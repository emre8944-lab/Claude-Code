"""Métadonnées SEO, FAQ et structure des pages."""

SERVICES = [
    dict(slug='plomberie', file='plomberie.html', name='Plomberie', label='Plomberie', num='01', icon='drop',
         short="Fuites, chauffe-eau, sanitaires et réseaux d'eau."),
    dict(slug='electricite', file='electricite.html', name='Électricité', label='Électricité', num='02', icon='bolt',
         short='Mise aux normes, tableau électrique, éclairage.'),
    dict(slug='carrelage', file='carrelage.html', name='Carrelage', label='Carrelage', num='03', icon='grid',
         short="Sols, faïence, grands formats, douches à l'italienne."),
    dict(slug='placo', file='placo-platrerie.html', name='Placo & plâtrerie', label='Placo', num='04', icon='layers',
         short='Cloisons, faux plafonds, doublages et isolation.'),
    dict(slug='renovation', file='renovation-interieure.html', name='Rénovation intérieure', label='Rénovation', num='05', icon='home',
         short='Salle de bain, cuisine, logement complet.'),
]
SVC = {s['slug']: s for s in SERVICES}

FAQ_HOME = [
    ('Le devis est-il vraiment gratuit ?',
     '<p>Oui. Le déplacement, la visite technique et le devis détaillé sont gratuits et sans engagement. '
     'Vous recevez votre devis sous 48 h après la visite.</p>'),
    ('Intervenez-vous pour de petits travaux ?',
     "<p>Oui : remplacement d'un chauffe-eau, ajout de prises, réparation d'une fuite, reprise de quelques m² "
     "de carrelage… Aucun chantier n'est trop petit pour être bien fait.</p>"),
    ("Quels sont vos délais d'intervention ?",
     '<p>Pour un dépannage (fuite, panne électrique), nous faisons le maximum pour intervenir rapidement. '
     'Pour un chantier, la date de démarrage et la durée des travaux sont fixées noir sur blanc à la signature du devis.</p>'),
    ('Êtes-vous assurés ?',
     '<p>Oui. Nous sommes couverts par une assurance responsabilité civile professionnelle et par une garantie décennale. '
     "L'attestation d'assurance est jointe à chaque devis.</p>"),
    ('Puis-je bénéficier d\'une TVA réduite ?',
     "<p>Pour des travaux de rénovation dans un logement achevé depuis plus de 2 ans, la TVA peut être de 10 % au lieu de 20 %, "
     "voire de 5,5 % pour certains travaux d'amélioration énergétique. Nous vérifions votre éligibilité avec vous "
     "et appliquons le bon taux directement sur le devis.</p>"),
    ('Comment se passe le paiement ?',
     '<p>Un acompte de %PH:30% % est demandé à la signature du devis, et le solde à la réception des travaux. '
     'Nous acceptons %PH:virement, chèque, carte bancaire%.</p>'),
]

FAQ_PLOMBERIE = [
    ('Intervenez-vous en urgence pour une fuite ?',
     "<p>Oui, appelez-nous directement au %TEL%. En attendant, coupez l'arrivée d'eau générale "
     "(le robinet se trouve généralement près du compteur). Nous faisons le maximum pour intervenir rapidement "
     "à %VILLE% et dans les environs.</p>"),
    ("Combien coûte le remplacement d'un chauffe-eau ?",
     "<p>Le prix dépend de la capacité (de 100 à 300 litres en général), du type d'appareil et de l'accessibilité "
     "de l'emplacement. Nous établissons un devis gratuit après avoir vu l'installation : le prix annoncé est le prix payé.</p>"),
    ('Pouvez-vous remplacer mes vieux tuyaux en plomb ?',
     '<p>Oui. Les canalisations en plomb doivent être remplacées : nous refaisons le réseau en cuivre ou en multicouche, '
     'en limitant au maximum les dégâts sur vos murs et vos sols.</p>'),
    ('Faites-vous aussi le carrelage après les travaux de plomberie ?',
     "<p>Oui, c'est tout l'intérêt : plomberie, électricité, placo et carrelage sont réalisés par la même équipe. "
     'Pas de coordination à gérer, un seul devis, un seul responsable.</p>'),
]

FAQ_ELEC = [
    ('Mon installation est ancienne, dois-je tout refaire ?',
     '<p>Pas forcément. Une mise en sécurité ciblée (tableau, prise de terre, protections différentielles) suffit souvent. '
     'Nous faisons un diagnostic et vous proposons des priorités, avec un budget par étape.</p>'),
    ("Qu'est-ce que la norme NF C 15-100 ?",
     "<p>C'est la norme qui encadre les installations électriques des logements en France : nombre de prises par pièce, "
     'protections, section des câbles, volumes de sécurité dans la salle de bain… Tous nos travaux la respectent.</p>'),
    ('Mon disjoncteur saute régulièrement, que faire ?',
     "<p>Cela peut venir d'un appareil défectueux, d'un circuit surchargé ou d'un défaut d'isolement. Débranchez les "
     'appareils du circuit concerné et appelez-nous : nous cherchons la cause au lieu de simplement réarmer.</p>'),
    ('Pouvez-vous fournir une attestation de conformité ?',
     "<p>Lorsqu'une attestation de conformité visée par le Consuel est nécessaire (installation neuve, rénovation "
     'totale), nous préparons le dossier pour vous.</p>'),
]

FAQ_CARRELAGE = [
    ("Pouvez-vous poser le carrelage que j'ai acheté moi-même ?",
     "<p>Oui. Nous vérifions simplement avec vous qu'il est adapté à l'usage (sol, mur, extérieur, pièce humide) "
     'et que la quantité prévue est suffisante.</p>'),
    ('Peut-on poser du carrelage sur un ancien carrelage ?',
     "<p>Souvent oui, si l'ancien revêtement est bien adhérent et plan, avec un primaire adapté. Nous vérifions "
     "l'état du support lors de la visite et vous conseillons la solution la plus durable.</p>"),
    ('Combien de temps faut-il pour carreler une pièce ?',
     '<p>Pour une pièce standard, comptez généralement quelques jours, en incluant la préparation du support, '
     'la pose et les joints. Nous vous donnons un planning précis avec le devis.</p>'),
    ('Quel entretien pour les joints ?',
     "<p>Un nettoyage régulier à l'eau savonneuse suffit. Dans les douches, un joint époxy, plus résistant "
     "aux taches et à l'humidité, est une bonne option : on en parle lors du devis.</p>"),
]

FAQ_PLACO = [
    ('Combien de temps pour monter une cloison ?',
     "<p>L'ossature et les plaques d'une cloison standard se posent souvent en une journée ; il faut ensuite compter "
     'le temps des bandes et enduits, qui demandent plusieurs passes avec séchage. Le planning précis figure dans le devis.</p>'),
    ('Peut-on accrocher des meubles lourds sur du placo ?',
     '<p>Oui, avec des chevilles adaptées ou, mieux, des renforts intégrés dans la cloison au moment du montage. '
     'Signalez-nous vos projets (meubles de cuisine, TV murale) : on les anticipe.</p>'),
    ('Le doublage isolant améliore-t-il vraiment le confort ?',
     '<p>Oui. Un mur non isolé est une source importante de déperdition de chaleur et de sensation de paroi froide. '
     "Un doublage isolant améliore nettement le confort et réduit les besoins de chauffage. Nous vous conseillons "
     "l'épaisseur adaptée à votre logement.</p>"),
    ('Faites-vous la peinture après le placo ?',
     '<p>Oui, nous pouvons prendre en charge les finitions jusqu\'à la peinture, pour vous livrer une pièce terminée.</p>'),
]

FAQ_RENO = [
    ("Combien coûte la rénovation d'une salle de bain ?",
     "<p>Le budget dépend surtout de la surface, des équipements choisis et de l'état des réseaux existants. "
     'Après la visite, nous vous remettons un devis détaillé poste par poste, avec des options si vous souhaitez ajuster.</p>'),
    ('Dois-je quitter mon logement pendant les travaux ?',
     "<p>Pas nécessairement. Pour une salle de bain ou une cuisine, nous organisons le chantier pour limiter la gêne "
     "(coupures d'eau et d'électricité annoncées à l'avance). Pour une rénovation complète, nous en discutons ensemble.</p>"),
    ('Qui est responsable si un problème survient ?',
     "<p>Nous. C'est l'avantage d'une entreprise unique : un seul interlocuteur, un seul contrat, et l'ensemble "
     'des travaux couvert par notre garantie décennale.</p>'),
    ("Pouvez-vous nous conseiller sur l'agencement et les matériaux ?",
     "<p>Oui, c'est le « Conseils » de notre nom. Nous vous aidons à optimiser l'espace, à choisir des matériaux "
     'durables et adaptés à votre budget, et nous vous orientons vers des fournisseurs de confiance.</p>'),
]

PAGES = [
    dict(
        file='index.html',
        title='Plombier, électricien, carreleur à [Ville] | USTA Conseils & Travaux',
        og_title='USTA Conseils & Travaux — rénovation tous corps d\'état à [Ville]',
        description="Entreprise familiale de rénovation à [Ville] : plomberie, électricité, carrelage, placo. "
                    "Un seul interlocuteur, devis gratuit sous 48 h, garantie décennale.",
        faqs=FAQ_HOME,
        cta=('Parlons de votre <em>projet.</em>',
             'Appelez-nous ou laissez vos coordonnées : on vous rappelle sous 24 h ouvrées '
             'avec de premiers conseils, gratuitement et sans engagement.'),
        track='accueil',
    ),
    dict(
        file='plomberie.html',
        title='Plombier à [Ville] – Installation, rénovation, dépannage | USTA',
        description="Plombier à [Ville] : recherche de fuite, chauffe-eau, sanitaires, salle de bain. "
                    "Entreprise familiale, devis gratuit sous 48 h, garantie décennale.",
        crumb='Plomberie', section='metiers', service=SVC['plomberie'], faqs=FAQ_PLOMBERIE,
        devis_href='contact.html?service=plomberie', track='plomberie',
        cta=('Besoin d\'un <em>plombier ?</em>',
             'Dépannage, remplacement ou projet de salle de bain : décrivez-nous votre besoin, '
             'on vous rappelle sous 24 h ouvrées.'),
    ),
    dict(
        file='electricite.html',
        title='Électricien à [Ville] – Mise aux normes, rénovation | USTA',
        description="Électricien à [Ville] : mise aux normes NF C 15-100, tableau électrique, rénovation complète, "
                    "éclairage, dépannage. Devis gratuit sous 48 h, garantie décennale.",
        crumb='Électricité', section='metiers', service=SVC['electricite'], faqs=FAQ_ELEC,
        devis_href='contact.html?service=electricite', track='electricite',
        cta=('Une installation <em>à sécuriser ?</em>',
             'Parlez-nous de votre logement : nous vous proposons un diagnostic clair et des priorités chiffrées.'),
    ),
    dict(
        file='carrelage.html',
        title='Carreleur à [Ville] – Pose de carrelage et faïence | USTA',
        description="Carreleur à [Ville] : carrelage de sol et mural, faïence, grands formats, douche à l'italienne, "
                    "terrasse. Visite conseil et devis gratuits, garantie décennale.",
        crumb='Carrelage', section='metiers', service=SVC['carrelage'], faqs=FAQ_CARRELAGE,
        devis_href='contact.html?service=carrelage', track='carrelage',
        cta=('Un sol <em>à carreler ?</em>',
             'Envoyez-nous la surface et quelques photos : on vous conseille sur les formats et on vous chiffre la pose.'),
    ),
    dict(
        file='placo-platrerie.html',
        title='Plaquiste à [Ville] – Cloisons, faux plafonds, doublage | USTA',
        description="Plaquiste à [Ville] : cloisons en placo, faux plafonds, doublage et isolation des murs, "
                    "bandes et finitions. Devis gratuit sous 48 h, garantie décennale.",
        crumb='Placo &amp; plâtrerie', section='metiers', service=SVC['placo'], faqs=FAQ_PLACO,
        devis_href='contact.html?service=placo', track='placo',
        cta=('Un espace <em>à redessiner ?</em>',
             "Une pièce en plus, un plafond à refaire, un mur à isoler : décrivez-nous votre projet, "
             "on vous rappelle sous 24 h ouvrées."),
    ),
    dict(
        file='renovation-interieure.html',
        title='Rénovation intérieure à [Ville] – Salle de bain, cuisine | USTA',
        description="Rénovation clé en main à [Ville] : salle de bain, cuisine, appartement ou maison. "
                    "Plomberie, électricité, placo et carrelage par une seule équipe. Devis gratuit.",
        crumb='Rénovation intérieure', section='renovation', service=SVC['renovation'], faqs=FAQ_RENO,
        devis_href='contact.html?service=renovation', track='renovation',
        cta=('Parlons de votre <em>rénovation.</em>',
             'Une visite gratuite pour comprendre vos envies, un devis global sous 48 h, '
             'et un seul interlocuteur jusqu\'à la fin du chantier.'),
    ),
    dict(
        file='contact.html',
        title='Devis gratuit – Contact | USTA Conseils & Travaux, [Ville]',
        description="Demandez votre devis gratuit pour vos travaux de plomberie, électricité, carrelage, placo "
                    "ou rénovation à [Ville]. Réponse sous 24 h ouvrées.",
        crumb='Devis gratuit', schema_type='ContactPage', devis_href='#formulaire',
    ),
    dict(
        file='mentions-legales.html',
        title='Mentions légales et données personnelles | USTA Conseils & Travaux',
        description='Mentions légales, informations sur l\'assurance décennale et politique de protection '
                    'des données personnelles de USTA Conseils & Travaux.',
        crumb='Mentions légales', noindex=True,
    ),
    dict(
        file='merci.html',
        title='Merci pour votre demande | USTA Conseils & Travaux',
        description='Votre demande de devis a bien été envoyée. Nous vous rappelons sous 24 h ouvrées.',
        noindex=True,
    ),
    dict(
        file='404.html',
        title='Page introuvable | USTA Conseils & Travaux',
        description="Cette page n'existe pas ou a été déplacée.",
        noindex=True, base='/',
    ),
]
