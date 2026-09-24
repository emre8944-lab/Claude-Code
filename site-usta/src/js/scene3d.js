/*
 * USTA — scène 3D « la maison éclatée »
 * Une pièce en coupe où chaque corps de métier est une couche :
 * carrelage (sol), plomberie (réseau bleu), électricité (circuits jaunes),
 * placo (cloisons et ossature), et la toiture orange du logo qui flotte au-dessus.
 *
 * Usage : <div data-scene3d data-focus="plomberie"> … </div>
 *   - sans data-focus : les métiers sont mis en avant tour à tour (accueil)
 *   - avec data-focus : un seul métier est mis en avant (pages métiers)
 *   - boutons [data-layer="…"] dans le même bloc hero : survol = mise en avant
 */
import {
  AmbientLight, BoxGeometry, CatmullRomCurve3, Color, CylinderGeometry,
  DirectionalLight, EdgesGeometry, Fog, GridHelper, Group, HemisphereLight, InstancedMesh,
  LineBasicMaterial, LineSegments, MathUtils, Matrix4, Mesh, MeshStandardMaterial, NeutralToneMapping,
  PCFShadowMap, PerspectiveCamera, PointLight, Scene, SphereGeometry, SRGBColorSpace,
  TubeGeometry, Vector3, WebGLRenderer,
} from 'three';

const COLORS = {
  ink: 0x0e0e0c,
  slab: 0x2b2a26,
  tile: 0xe7e2d8,
  plaster: 0xeeebe4,
  stud: 0x9aa3ad,
  white: 0xf5f3ef,
  panel: 0x3a3934,
  roof: 0xff4f14,
  plomberie: 0x3d7bff,
  electricite: 0xffc53d,
  carrelage: 0x2bb5a0,
  placo: 0xc9c4b8,
};

const ORDER = ['carrelage', 'plomberie', 'electricite', 'placo', 'toiture'];
const CYCLE = ['plomberie', 'electricite', 'carrelage', 'placo'];

const easeOut = (t) => 1 - Math.pow(1 - t, 3);
const damp = (a, b, lambda, dt) => MathUtils.lerp(a, b, 1 - Math.exp(-lambda * dt));

function mat(color, opts = {}) {
  const m = new MeshStandardMaterial({
    color, roughness: 0.75, metalness: 0, transparent: true,
    emissiveIntensity: opts.emissive !== undefined ? 1 : 0, ...opts,
  });
  m.userData.highlight = true; // s'illumine quand sa couche est mise en avant
  return m;
}

/* ------------------------------------------------------------------ modèle */

function buildModel() {
  const layers = {};
  const edgeMat = new LineBasicMaterial({ color: COLORS.ink, transparent: true, opacity: 0.35 });

  function layer(key, color) {
    const group = new Group();
    group.name = key;
    layers[key] = { key, group, color: new Color(color), mats: new Set(), edges: [], lift: 0, anchor: new Vector3(), particles: [] };
    return layers[key];
  }

  function add(l, geometry, material, x, y, z, { edges = true, cast = true, receive = false, rot } = {}) {
    const mesh = new Mesh(geometry, material);
    mesh.position.set(x, y, z);
    if (rot) mesh.rotation.set(rot[0], rot[1], rot[2]);
    mesh.castShadow = cast;
    mesh.receiveShadow = receive;
    l.group.add(mesh);
    l.mats.add(material);
    if (edges) {
      const e = new LineSegments(new EdgesGeometry(geometry, 25), edgeMat.clone());
      e.position.copy(mesh.position);
      e.rotation.copy(mesh.rotation);
      l.group.add(e);
      l.edges.push(e.material);
    }
    return mesh;
  }

  function pipe(l, points, radius, material, particleColor) {
    const curve = new CatmullRomCurve3(points.map((p) => new Vector3(...p)), false, 'catmullrom', 0.08);
    const mesh = new Mesh(new TubeGeometry(curve, points.length * 24, radius, 10, false), material);
    mesh.castShadow = true;
    l.group.add(mesh);
    l.mats.add(material);
    // petites impulsions lumineuses qui circulent dans le réseau (eau / courant)
    const pm = new MeshStandardMaterial({ color: particleColor, emissive: particleColor, emissiveIntensity: 2.2, transparent: true });
    for (let i = 0; i < 3; i++) {
      const dot = new Mesh(new SphereGeometry(radius * 1.35, 12, 12), pm);
      l.group.add(dot);
      l.particles.push({ mesh: dot, curve, t: i / 3 });
    }
    l.mats.add(pm);
    return curve;
  }

  /* Sol : dalle + carrelage */
  const floor = layer('carrelage', COLORS.carrelage);
  add(floor, new BoxGeometry(4.3, 0.22, 3.3), mat(COLORS.slab, { roughness: 0.95 }), 0, -0.11, 0, { receive: true, cast: false });
  const tileMat = mat(COLORS.tile, { roughness: 0.45 });
  const tiles = new InstancedMesh(new BoxGeometry(0.56, 0.05, 0.56), tileMat, 35);
  const m4 = new Matrix4();
  let n = 0;
  for (let i = 0; i < 7; i++) for (let j = 0; j < 5; j++) {
    m4.makeTranslation(-1.8 + i * 0.6, 0.025, -1.2 + j * 0.6);
    tiles.setMatrixAt(n++, m4);
  }
  tiles.receiveShadow = true;
  floor.group.add(tiles);
  floor.mats.add(tileMat);
  floor.anchor.set(1.9, 0.1, 1.45);

  /* Plomberie : arrivée, lavabo, douche, chauffe-eau */
  const plumb = layer('plomberie', COLORS.plomberie);
  const pipeMat = mat(COLORS.plomberie, { roughness: 0.3, metalness: 0.25 });
  const drainMat = mat(0x8c96a6, { roughness: 0.5, metalness: 0.1 });
  pipe(plumb, [[-2.1, 0.12, -1.38], [-1.2, 0.12, -1.38], [-0.9, 0.12, -1.38], [-0.9, 0.5, -1.38], [-0.9, 0.78, -1.38]], 0.045, pipeMat, 0x9cc0ff);
  pipe(plumb, [[-1.2, 0.12, -1.38], [-1.2, 0.12, -1.3], [0.55, 0.12, -1.3], [0.55, 0.9, -1.38], [0.55, 1.95, -1.38], [0.55, 1.95, -1.15]], 0.04, pipeMat, 0x9cc0ff);
  pipe(plumb, [[-1.65, 0.12, -1.38], [-1.65, 0.8, -1.38]], 0.04, pipeMat, 0x9cc0ff);
  pipe(plumb, [[-0.75, 0.62, -1.36], [-0.75, 0.2, -1.36], [-0.75, 0.2, -1.0], [0.1, 0.2, -1.0]], 0.06, drainMat, 0xd6dde8);
  add(plumb, new BoxGeometry(0.7, 0.16, 0.45), mat(COLORS.white, { roughness: 0.3 }), -0.9, 0.86, -1.22);
  add(plumb, new CylinderGeometry(0.26, 0.26, 0.95, 28), mat(COLORS.white, { roughness: 0.35 }), -1.65, 1.3, -1.2);
  add(plumb, new CylinderGeometry(0.265, 0.265, 0.1, 28), mat(COLORS.plomberie, { roughness: 0.4 }), -1.65, 1.62, -1.2, { edges: false });
  add(plumb, new CylinderGeometry(0.12, 0.12, 0.03, 24), mat(0xc9ced6, { metalness: 0.6, roughness: 0.3 }), 0.55, 1.9, -1.1, { edges: false });
  add(plumb, new BoxGeometry(1.0, 0.05, 1.0), mat(COLORS.white, { roughness: 0.3 }), 0.5, 0.075, -1.0, { cast: false, receive: true });
  plumb.anchor.set(-1.65, 1.85, -1.2);

  /* Électricité : tableau, circuits, prises, suspension */
  const elec = layer('electricite', COLORS.electricite);
  const wireMat = mat(COLORS.electricite, { roughness: 0.5, emissive: COLORS.electricite, emissiveIntensity: 0.15 });
  add(elec, new BoxGeometry(0.42, 0.58, 0.1), mat(COLORS.panel, { roughness: 0.6 }), 1.72, 1.45, -1.45);
  add(elec, new BoxGeometry(0.34, 0.06, 0.02), mat(COLORS.electricite, { emissive: COLORS.electricite, emissiveIntensity: 0.4 }), 1.72, 1.58, -1.39, { edges: false });
  pipe(elec, [[1.72, 1.74, -1.44], [1.72, 2.25, -1.44], [0.2, 2.25, -1.44], [-0.35, 2.25, -1.44], [-0.35, 0.45, -1.44]], 0.02, wireMat, 0xfff1b8);
  pipe(elec, [[1.6, 1.16, -1.44], [1.6, 0.3, -1.44], [-1.98, 0.3, -1.44], [-1.98, 0.3, 0.9]], 0.02, wireMat, 0xfff1b8);
  pipe(elec, [[0.2, 2.25, -1.44], [0.2, 2.25, -0.2], [0.2, 1.95, -0.2]], 0.015, wireMat, 0xfff1b8);
  add(elec, new BoxGeometry(0.14, 0.14, 0.04), mat(COLORS.white), -0.35, 0.42, -1.47);
  add(elec, new BoxGeometry(0.04, 0.14, 0.14), mat(COLORS.white), -1.97, 0.35, 0.9);
  add(elec, new CylinderGeometry(0.03, 0.2, 0.18, 24, 1, true), mat(COLORS.panel, { side: 2 }), 0.2, 1.88, -0.2, { edges: false });
  const bulbMat = new MeshStandardMaterial({ color: 0xfff4d6, emissive: 0xffd27a, emissiveIntensity: 3, transparent: true });
  const bulb = new Mesh(new SphereGeometry(0.07, 16, 16), bulbMat);
  bulb.position.set(0.2, 1.8, -0.2);
  elec.group.add(bulb);
  elec.mats.add(bulbMat);
  const lamp = new PointLight(0xffc98a, 2.2, 4.5, 1.6);
  lamp.position.set(0.2, 1.75, -0.2);
  elec.group.add(lamp);
  elec.anchor.set(1.72, 1.9, -1.45);

  /* Placo : murs, fenêtre, cloison en cours de montage */
  const wall = layer('placo', COLORS.placo);
  const plaster = mat(COLORS.plaster, { roughness: 0.9 });
  add(wall, new BoxGeometry(4.3, 2.44, 0.1), plaster, 0, 1.22, -1.6, { receive: true });
  add(wall, new BoxGeometry(0.1, 0.9, 3.3), plaster, -2.1, 0.45, 0, { receive: true });
  add(wall, new BoxGeometry(0.1, 0.64, 3.3), plaster, -2.1, 2.12, 0, { receive: true });
  add(wall, new BoxGeometry(0.1, 0.9, 1.25), plaster, -2.1, 1.35, -1.025, { receive: true });
  add(wall, new BoxGeometry(0.1, 0.9, 1.05), plaster, -2.1, 1.35, 1.125, { receive: true });
  add(wall, new BoxGeometry(0.02, 0.9, 1.0), mat(0x9fc3ff, { opacity: 0.22, roughness: 0.1 }), -2.1, 1.35, 0.1, { cast: false });
  const studMat = mat(COLORS.stud, { metalness: 0.6, roughness: 0.35 });
  // cloison en cours de montage : ossature métallique + une plaque posée
  for (const z of [-1.5, -1.1, -0.7]) add(wall, new BoxGeometry(0.05, 2.4, 0.07), studMat, 1.35, 1.2, z, { edges: false });
  add(wall, new BoxGeometry(0.06, 0.05, 0.9), studMat, 1.35, 0.03, -1.1, { edges: false });
  add(wall, new BoxGeometry(0.06, 0.05, 0.9), studMat, 1.35, 2.4, -1.1, { edges: false });
  add(wall, new BoxGeometry(0.025, 2.4, 0.45), plaster, 1.395, 1.2, -1.3);
  wall.anchor.set(1.38, 2.45, -0.7);

  /* Toiture : le chevron orange du logo, en lévitation */
  const roof = layer('toiture', COLORS.roof);
  const roofMat = mat(COLORS.roof, { roughness: 0.55 });
  add(roof, new BoxGeometry(4.7, 0.1, 2.05), roofMat, 0, 3.25, 0.87, { rot: [Math.PI / 6, 0, 0] });
  add(roof, new BoxGeometry(4.7, 0.1, 2.05), roofMat, 0, 3.25, -0.87, { rot: [-Math.PI / 6, 0, 0] });
  roof.anchor.set(0, 3.8, 0);

  return layers;
}

/* ------------------------------------------------------------------ scène */

function webglAvailable() {
  try {
    const c = document.createElement('canvas');
    return !!(window.WebGLRenderingContext && (c.getContext('webgl2') || c.getContext('webgl')));
  } catch (e) {
    return false;
  }
}

function init(host) {
  if (!webglAvailable()) {
    host.classList.add('is-fallback');
    return;
  }
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const small = window.innerWidth < 760;
  const focus = host.getAttribute('data-focus');
  const stage = host.querySelector('.scene3d__stage') || host;

  const renderer = new WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, small ? 1.5 : 1.75));
  renderer.outputColorSpace = SRGBColorSpace;
  renderer.toneMapping = NeutralToneMapping;
  renderer.toneMappingExposure = 1;
  renderer.shadowMap.enabled = !small;
  renderer.shadowMap.type = PCFShadowMap;
  renderer.domElement.setAttribute('aria-hidden', 'true');
  stage.appendChild(renderer.domElement);

  const scene = new Scene();
  scene.fog = new Fog(COLORS.ink, 16, 30);
  const camera = new PerspectiveCamera(28, 1, 0.1, 100);
  const target = new Vector3(0, 2.25, 0);

  scene.add(new HemisphereLight(0xffffff, 0x2a2926, 1.1));
  scene.add(new AmbientLight(0xffffff, 0.15));
  const key = new DirectionalLight(0xfff3e4, 2.4);
  key.position.set(6, 10, 7);
  key.castShadow = true;
  key.shadow.mapSize.set(1024, 1024);
  key.shadow.camera.left = -5; key.shadow.camera.right = 5;
  key.shadow.camera.top = 6; key.shadow.camera.bottom = -4;
  key.shadow.bias = -0.0008;
  scene.add(key);
  const rim = new DirectionalLight(0x8fb3ff, 0.9);
  rim.position.set(-8, 5, -6);
  scene.add(rim);

  const grid = new GridHelper(18, 36, 0x55544e, 0x33322e);
  grid.position.y = -0.23;
  grid.material.transparent = true;
  grid.material.opacity = 0.35;
  scene.add(grid);

  const model = new Group();
  const layers = buildModel();
  ORDER.forEach((k) => model.add(layers[k].group));
  scene.add(model);

  // Étiquettes HTML liées aux couches
  const labels = {};
  host.querySelectorAll('.scene3d__label[data-layer]').forEach((el) => { labels[el.getAttribute('data-layer')] = el; });
  const chips = document.querySelectorAll('[data-scene-chip][data-layer]');

  const tmp = new Vector3();

  // Boucle de rendu (en pause hors écran ou onglet masqué)
  let running = false;
  let visible = true;
  let last = performance.now();
  let settleFrames = 0;

  // État
  let active = focus || null;
  let cycleIndex = 0;
  let cycleTimer = 0;
  let pausedUntil = 0;
  let intro = reduced ? 1 : 0;
  let introStart = 0;
  let explode = 0;
  const pointer = { x: 0, y: 0, tx: 0, ty: 0 };
  const baseRotation = -0.5;

  function setActive(k) {
    active = k;
    chips.forEach((c) => c.classList.toggle('is-active', c.getAttribute('data-layer') === k));
  }
  if (focus) setActive(focus);

  chips.forEach((chip) => {
    const k = chip.getAttribute('data-layer');
    const on = () => { setActive(k); pausedUntil = performance.now() + 6000; wake(); };
    chip.addEventListener('mouseenter', on);
    chip.addEventListener('focus', on);
    chip.addEventListener('click', on);
  });

  // Souris : légère rotation de la maquette
  const heroEl = host.closest('.hero, .page-hero') || host;
  heroEl.addEventListener('pointermove', (e) => {
    const r = heroEl.getBoundingClientRect();
    pointer.tx = ((e.clientX - r.left) / r.width - 0.5) * 2;
    pointer.ty = ((e.clientY - r.top) / r.height - 0.5) * 2;
    wake();
  });
  heroEl.addEventListener('pointerleave', () => { pointer.tx = 0; pointer.ty = 0; wake(); });

  // Défilement : la maison « s'éclate » en couches quand on descend
  function onScroll() {
    if (window.innerWidth >= 960) {
      // grand écran : la scène occupe tout le hero, elle défile moins vite (parallaxe) et s'éclate
      const r = heroEl.getBoundingClientRect();
      view.scroll = Math.max(0, -r.top);
      explode = MathUtils.clamp(-r.top / (r.height * 0.6), 0, 1);
    } else {
      // mobile : la scène est un bloc dans la page, elle s'éclate quand elle passe le milieu de l'écran
      const r = host.getBoundingClientRect();
      view.scroll = 0;
      explode = MathUtils.clamp((window.innerHeight * 0.45 - r.top) / (r.height * 1.2), 0, 1) * 0.7;
    }
    placeCamera();
    wake();
  }
  window.addEventListener('scroll', onScroll, { passive: true });

  // Cadrage : sur grand écran la maquette se place à droite du texte (data-offset = position horizontale)
  const view = { dist: 17, unitsPerPx: 0.01, scroll: 0 };
  const dir = new Vector3(0.66, 0.46, 0.72).normalize();

  function placeCamera() {
    const lift = view.scroll * view.unitsPerPx * 0.55; // parallaxe : la maquette défile moins vite que la page
    camera.position.copy(target).addScaledVector(dir, view.dist);
    camera.position.y += lift;
    tmp.copy(target);
    tmp.y += lift;
    camera.lookAt(tmp);
  }

  function resize() {
    const w = stage.clientWidth || 1;
    const h = stage.clientHeight || 1;
    const wide = window.innerWidth >= 960;
    const offset = wide ? parseFloat(host.getAttribute('data-offset') || '0.5') : 0.5;
    const size = parseFloat(host.getAttribute('data-size') || '1');
    const frameW = offset > 0.5 ? w * 2 * offset : w;
    renderer.setSize(w, h, false);
    camera.aspect = frameW / h;
    camera.setViewOffset(frameW, h, 0, 0, w, h);
    // recule la caméra sur les formats étroits pour garder toute la maquette
    view.dist = MathUtils.clamp(19 / Math.min((wide ? w * 0.55 : w) / h, 1.2), 15, 34) / size;
    view.unitsPerPx = (2 * view.dist * Math.tan(MathUtils.degToRad(camera.fov / 2))) / h;
    camera.updateProjectionMatrix();
    placeCamera();
    wake();
  }
  new ResizeObserver(resize).observe(stage);


  function wake() {
    settleFrames = 90;
    if (!running && visible && !document.hidden) {
      running = true;
      last = performance.now();
      requestAnimationFrame(frame);
    }
  }

  new IntersectionObserver((entries) => {
    visible = entries[0].isIntersecting;
    if (visible) wake();
  }).observe(host);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) wake(); });

  function frame(now) {
    const dt = MathUtils.clamp((now - last) / 1000, 0, 0.05); // rAF peut précéder performance.now()
    last = now;
    const time = now / 1000;

    // intro : les couches se posent l'une après l'autre (basée sur l'horloge, pas sur le nombre d'images,
    // pour durer 2,2 s même sur un appareil lent)
    if (intro < 1) {
      if (!introStart) introStart = now;
      intro = Math.min(1, (now - introStart) / 2200);
    }

    // cycle automatique des métiers (accueil)
    if (!focus && !reduced && intro >= 1 && now > pausedUntil) {
      cycleTimer += dt;
      if (cycleTimer > 2.8 || active === null) {
        cycleTimer = 0;
        setActive(CYCLE[cycleIndex++ % CYCLE.length]);
      }
    }

    pointer.x = damp(pointer.x, pointer.tx, 4, dt);
    pointer.y = damp(pointer.y, pointer.ty, 4, dt);
    const idle = reduced ? 0 : Math.sin(time * 0.35) * 0.12;
    model.rotation.y = baseRotation + idle + pointer.x * 0.28;
    model.rotation.x = pointer.y * 0.05;

    ORDER.forEach((k, i) => {
      const l = layers[k];
      const isActive = active === k;
      const t = MathUtils.clamp(intro * 1.6 - i * 0.14, 0, 1);
      const drop = (1 - easeOut(t)) * (3 + i * 0.6);
      const float = k === 'toiture' ? 1.45 + (reduced ? 0 : Math.sin(time * 1.2) * 0.08) : 0;
      l.lift = damp(l.lift, isActive ? 0.28 : 0, 6, dt);
      l.group.position.y = drop + float + l.lift + explode * (i - 1.5) * 0.6;

      const dim = active && !isActive && k !== 'toiture' ? 0.72 : 1;
      const alpha = easeOut(t) * dim;
      l.mats.forEach((m) => {
        if (m.userData.baseOpacity === undefined) {
          m.userData.baseOpacity = m.opacity;
          m.userData.baseGlow = m.emissiveIntensity;
        }
        m.opacity = m.userData.baseOpacity * alpha;
        if (m.userData.highlight) {
          if (k !== 'electricite') m.emissive.copy(l.color);
          m.emissiveIntensity = damp(m.emissiveIntensity, m.userData.baseGlow + (isActive ? 0.25 : 0), 6, dt);
        }
      });
      l.edges.forEach((e) => { e.opacity = 0.35 * alpha; });

      l.particles.forEach((p) => {
        p.t = (p.t + dt * (isActive ? 0.32 : 0.16)) % 1;
        p.curve.getPointAt(p.t, p.mesh.position);
        p.mesh.visible = !reduced;
      });

      const label = labels[k];
      if (label) {
        tmp.copy(l.anchor);
        l.group.localToWorld(tmp);
        tmp.project(camera);
        const x = (tmp.x * 0.5 + 0.5) * stage.clientWidth;
        const y = (-tmp.y * 0.5 + 0.5) * stage.clientHeight;
        label.style.transform = `translate(${x.toFixed(1)}px, ${y.toFixed(1)}px)`;
        label.classList.toggle('is-flip', x > stage.clientWidth - 190);
        const showAll = explode > 0.35 && stage.clientWidth >= 700;
        label.classList.toggle('is-visible', intro >= 1 && (isActive || showAll));
      }
    });

    renderer.render(scene, camera);
    host.classList.add('is-ready');

    const animating = !reduced || intro < 1 || Math.abs(pointer.x - pointer.tx) > 0.001;
    if (settleFrames > 0) settleFrames--;
    if (visible && !document.hidden && (animating || settleFrames > 0)) {
      requestAnimationFrame(frame);
    } else {
      running = false;
    }
  }

  resize();
  onScroll();
  wake();
}

function start() {
  document.querySelectorAll('[data-scene3d]').forEach((el) => {
    try { init(el); } catch (e) { el.classList.add('is-fallback'); }
  });
}

if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
else start();
