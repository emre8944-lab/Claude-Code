"""Textes des pages métiers (gabarit src/pages/_service.html)."""

SERVICE_PAGES = {
    'plomberie': dict(
        h1='Plombier à %VILLE%',
        h1_small='Installation, rénovation et dépannage',
        lead="Fuite, chauffe-eau en panne, nouvelle salle de bain ou réseau à refaire : nous intervenons avec du matériel "
             "de qualité et un travail soigné, garanti par notre assurance décennale.",
        cta_label='Devis plomberie gratuit',
        urgent=('Fuite ou urgence ?', "Coupez l'eau, puis appelez-nous directement."),
        presta_title='Nos prestations<br><em>de plomberie.</em>',
        presta_intro="Du simple remplacement de robinet à la création complète d'un réseau, nous prenons en charge "
                     "tous vos travaux de plomberie sanitaire.",
        prestations=[
            ('Recherche et réparation de fuites', "Fuite visible ou cachée, compteur qui tourne, tache au plafond : nous localisons l'origine et réparons durablement."),
            ('Chauffe-eau et cumulus', 'Remplacement, installation ou entretien, avec un conseil honnête sur la capacité adaptée à votre foyer.'),
            ('Sanitaires et robinetterie', 'Pose et remplacement de WC (y compris suspendus), lavabos, éviers, mitigeurs, douches et baignoires.'),
            ('Création de salle de bain', "Arrivées d'eau, évacuations, douche à l'italienne : tout le réseau est prêt avant le carrelage."),
            ('Remplacement de canalisations', 'Réseaux vétustes en plomb ou en acier galvanisé remplacés par du cuivre ou du multicouche.'),
            ('Débouchage et entretien', 'Évier, WC ou canalisation bouchés : intervention propre, et des conseils pour éviter que cela recommence.'),
        ],
        adv_title='Un plombier qui pense<br><em>à la suite.</em>',
        adv_text="Parce que nous réalisons aussi l'électricité, le placo et le carrelage, nous anticipons tout ce qui vient après "
                 "la plomberie : passage des gaines, cloisons, pentes d'évacuation, finitions. Pas de carrelage cassé pour "
                 "rattraper un tuyau oublié.",
        adv_checks=['Un seul devis pour la plomberie et les finitions', "Des réseaux pensés pour durer et faciles d'accès",
                    'Un chantier rendu propre, testé et en service'],
        tip="Un chauffe-eau entartré chauffe moins bien et consomme davantage. Avant de le remplacer, un simple détartrage "
            "peut suffire : on vous dit honnêtement ce qui est le plus rentable pour vous.",
        faq_title='Plomberie :<br><em>vos questions.</em>',
    ),
    'electricite': dict(
        h1='Électricien à %VILLE%',
        h1_small='Mise aux normes, rénovation et dépannage',
        lead="Installation vieillissante, disjoncteur qui saute, projet de rénovation : nous rendons votre installation sûre, "
             "conforme à la norme NF C 15-100 et adaptée à vos usages d'aujourd'hui.",
        cta_label='Devis électricité gratuit',
        urgent=('Panne électrique ?', 'Ne réarmez pas en boucle : appelez-nous, on cherche la cause.'),
        presta_title="Nos prestations<br><em>d'électricité.</em>",
        presta_intro="Maison, appartement ou local professionnel : de l'ajout d'une prise à la rénovation complète, "
                     "nous réalisons tous vos travaux électriques.",
        prestations=[
            ('Mise en sécurité et aux normes', 'Installation ancienne, absence de terre, prises non protégées : nous sécurisons votre logement.'),
            ('Tableau électrique', 'Remplacement ou création de tableau, interrupteurs différentiels, repérage clair de chaque circuit.'),
            ('Rénovation électrique complète', "Refonte de l'installation d'un appartement ou d'une maison, coordonnée avec les cloisons."),
            ('Prises, interrupteurs et circuits', 'Ajout de prises, circuits spécialisés (four, plaque, lave-linge), prises réseau RJ45.'),
            ('Éclairage intérieur et extérieur', 'Spots encastrés, LED, éclairage de façade ou de jardin, variateurs et détecteurs.'),
            ('Dépannage électrique', 'Panne, court-circuit, disjoncteur qui saute : recherche de la cause et réparation durable.'),
        ],
        adv_title='Une électricité pensée<br><em>avec le chantier.</em>',
        adv_text="Placer les prises au bon endroit, passer les gaines avant de fermer les cloisons, prévoir l'éclairage avant "
                 "le faux plafond : quand la même équipe réalise l'électricité et le placo, tout est plus propre, plus rapide "
                 "et moins cher.",
        adv_checks=['Plan des prises et éclairages validé avec vous', 'Pas de goulottes disgracieuses : tout est encastré',
                    'Tableau étiqueté et explications à la livraison'],
        tip="Vous vendez ou louez un logement dont l'installation a plus de 15 ans ? Un diagnostic électricité est "
            "obligatoire. Nous corrigeons les anomalies relevées pour que votre bien soit sûr et plus facile à vendre ou à louer.",
        faq_title='Électricité :<br><em>vos questions.</em>',
    ),
    'carrelage': dict(
        h1='Carreleur à %VILLE%',
        h1_small="Sols, murs et faïence posés dans les règles de l'art",
        lead="Un beau carrelage, c'est d'abord un support bien préparé, un calepinage réfléchi et des joints réguliers. "
             "Nous vous aidons à choisir les bons formats, puis nous le posons pour qu'il dure des décennies.",
        cta_label='Devis carrelage gratuit',
        urgent=('Pas encore choisi votre carrelage ?', 'On vous conseille sur place, avant même le devis.'),
        presta_title='Nos prestations<br><em>de carrelage.</em>',
        presta_intro='Intérieur ou extérieur, sol ou mur, petit ou grand format : nous posons tous types de carrelage '
                     'avec la même exigence.',
        prestations=[
            ('Carrelage de sol', 'Pièces de vie, cuisine, entrée : pose droite, décalée ou en diagonale, avec plinthes assorties.'),
            ('Faïence murale', 'Salle de bain, crédence de cuisine, WC : faïence, zellige, carreaux de ciment ou grands formats.'),
            ('Grands formats', 'Dalles de 60 × 120 cm et plus : double encollage, système de nivellement, planéité parfaite.'),
            ("Douche à l'italienne", "Pente d'écoulement, étanchéité sous carrelage, siphon ou caniveau : l'étanchéité avant l'esthétique."),
            ('Terrasses extérieures', 'Carrelage extérieur collé ou dalles sur plots, résistant au gel et antidérapant.'),
            ('Dépose et préparation', "Dépose de l'ancien revêtement, ragréage ou chape : un support sain, gage d'une pose durable."),
        ],
        adv_title='Se voit en dernier.<br><em>Se remarque en premier.</em>',
        adv_text="Parce que nous réalisons aussi la plomberie et le placo en amont, les évacuations, les niveaux et les angles "
                 "sont prévus pour le carrelage dès le départ. C'est la différence entre une pose correcte et une finition impeccable.",
        adv_checks=['Calepinage étudié pour éviter les petites coupes', "Supports hydrofuges et étanchéité dans les pièces d'eau",
                    'Joints adaptés à chaque usage'],
        tip="Prévoyez environ 10 % de carrelage en plus pour les coupes et la casse, et gardez quelques carreaux de côté : "
            "en cas de réparation dans quelques années, la même référence ne sera peut-être plus disponible.",
        faq_title='Carrelage :<br><em>vos questions.</em>',
    ),
    'placo': dict(
        h1='Plaquiste à %VILLE%',
        h1_small='Cloisons, faux plafonds et doublages',
        lead="Créer une chambre, cacher des gaines, isoler un mur froid ou intégrer des spots : la plaque de plâtre "
             "transforme vos espaces rapidement, proprement et avec un budget maîtrisé.",
        cta_label='Devis placo gratuit',
        urgent=("Besoin d'une pièce en plus ?", "Chambre, bureau, dressing : on étudie l'espace avec vous."),
        presta_title='Plâtrerie<br><em>et isolation.</em>',
        presta_intro='Plaques de plâtre, ossatures métalliques, isolants : nous réalisons vos aménagements intérieurs, '
                     "de l'ossature aux finitions.",
        prestations=[
            ('Cloisons de distribution', 'Création de chambres, bureau, dressing ou séparation de pièces, avec bloc-porte intégré.'),
            ('Faux plafonds', 'Plafonds suspendus pour masquer réseaux et poutres, intégrer des spots ou abaisser une hauteur.'),
            ('Doublage et isolation des murs', 'Doublage collé ou sur ossature avec isolant : plus de confort, moins de déperditions.'),
            ('Isolation acoustique', 'Cloisons et plafonds renforcés pour limiter les bruits entre pièces ou avec les voisins.'),
            ('Plaques pour pièces humides', 'Salle de bain et cuisine : plaques hydrofuges, prêtes à recevoir la faïence.'),
            ('Bandes, enduits et finitions', 'Joints invisibles, angles nets, surfaces prêtes à peindre. Nous pouvons aussi peindre.'),
        ],
        adv_title='Des murs qui accueillent<br><em>déjà les réseaux.</em>',
        adv_text="Avant de fermer une cloison, nous passons les gaines électriques et les réseaux d'eau exactement là où il "
                 "faut. Pas besoin de rouvrir un mur neuf pour ajouter une prise oubliée.",
        adv_checks=['Renforts prévus pour vos meubles et équipements lourds', 'Spots et éclairages intégrés dès la pose',
                    'Chantier protégé et nettoyé chaque jour'],
        tip="Dans une chambre ou un bureau, pensez à ajouter un isolant dans la cloison : pour un surcoût modeste, le gain "
            "de confort acoustique est considérable.",
        faq_title='Placo :<br><em>vos questions.</em>',
    ),
    'renovation': dict(
        h1='Rénovation intérieure à %VILLE%',
        h1_small='Salle de bain, cuisine, logement complet',
        lead="Vous avez un projet, nous gérons tout le reste : conseil, coordination des corps de métier, réalisation et "
             "finitions. Une seule entreprise, un seul devis, un seul responsable.",
        cta_label='Devis rénovation gratuit',
        urgent=('Un seul devis pour tout le chantier', 'Tous les métiers chiffrés ensemble, sans oubli.'),
        presta_title='Les projets que<br><em>nous réalisons.</em>',
        presta_intro='Parce que nous maîtrisons tous les métiers du second œuvre, nous prenons en charge votre projet de A à Z, '
                     'quelle que soit sa taille.',
        prestations=[
            ('Salle de bain clé en main', "Dépose, réseaux, placo hydrofuge, étanchéité, carrelage, meubles et sanitaires : douche à l'italienne, baignoire ou salle d'eau.", 'salle-de-bain'),
            ('Rénovation de cuisine', "Arrivées d'eau et évacuations, circuits électriques dédiés, crédence et sol : tout est prêt pour vos meubles.", 'cuisine'),
            ('Appartement ou maison complète', "Redistribution des pièces, remise à neuf de l'électricité et de la plomberie, isolation, sols et murs.", 'logement'),
            ('Avant location ou vente', 'Rafraîchissement, mise en sécurité électrique, petites réparations : nous valorisons votre bien.', 'location'),
            ('Adaptation au vieillissement', 'Douche de plain-pied, barres d\'appui, prises et interrupteurs à hauteur adaptée, éclairage renforcé.'),
            ('Finitions et petits travaux', 'Peinture, reprises, petites réparations : un chantier réussi se joue aussi dans les détails.'),
        ],
        adv_title='Chaque métier<br><em>au bon moment.</em>',
        adv_text="Pas de temps mort ni de retour en arrière. Voici l'enchaînement type d'une rénovation de salle de bain :",
        adv_timeline=[
            ('Protection et dépose', 'Sols et accès protégés, ancien équipement déposé et évacué.'),
            ('Plomberie et électricité', "Nouveaux réseaux d'eau et d'évacuation, circuits et éclairages."),
            ('Placo et étanchéité', 'Plaques hydrofuges, coffrages, étanchéité sous carrelage.'),
            ('Carrelage et faïence', 'Sol et murs, pente de douche, joints.'),
            ('Équipements et finitions', 'Meubles, sanitaires, robinetterie, peinture, nettoyage.'),
            ('Réception avec vous', 'Vérification ensemble, point par point, avant la remise des clés.'),
        ],
        tip="Fixez votre budget total dès le départ en gardant une marge d'environ 10 % pour les imprévus, surtout dans "
            "l'ancien. Nous construisons le devis autour de ce budget et vous indiquons où investir… et où économiser.",
        faq_title='Rénovation :<br><em>vos questions.</em>',
    ),
}
