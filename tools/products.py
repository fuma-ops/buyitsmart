# Pages produit « 10 questions avant d'acheter » (destinations des épingles Pinterest : 1 question = 1 épingle = 1 réponse).
# Faits vérifiés le 2026-11-11 : guide officiel Keurig « K-Mini Use & Care Guide » (dam.keurig.com) pour les caractéristiques,
# fiches revendeurs pour la largeur, avis clients et tests de presse traités comme des opinions.
# Exécuté depuis build.py après usecases.py (EXTRA_PAGES existe déjà).

KM_GUIDE = 'https://dam.keurig.com/content/dam/public-assets/support/kcom/pdf/KMini_UCG.pdf'
KM_URL = '/guides/coffee-maker/keurig-k-mini/'
KM_AFF = 'https://link.amazon/B0hgdV6Ne'
KM_Q = [
 ('worth-it', 'Is the Keurig K-Mini worth buying?',
  'Yes, if you drink one cup at a time, have little counter space and value speed over taste control. It is less of a fit if you brew for two or more people, want strong or espresso-style coffee, or don’t want to pay for pods every day.',
  'The K-Mini does one job: one fresh cup from a K-Cup pod, in a very narrow body. Its limits (one cup per fill, no strength setting) are the price of that small size.'),
 ('counter-space', 'How much counter space does it need?',
  'Very little in width: Keurig says it is less than 5 inches wide, and retailer specs list about 4.5 inches. Plan room above it too: you lift a lid to pour water and a handle to insert the pod.',
  'Retailer listings give about 12.1 in. high × 4.5 in. wide × 11.3 in. deep. Check the space under your wall cabinets with the handle raised before you buy.'),
 ('water-refill', 'Do you refill the water for every cup?',
  'Yes. There is no tank to keep filled: you pour the amount of water you want to brew (6 oz minimum, 12 oz maximum) into the reservoir each time. Keurig’s guide suggests measuring it with your mug.',
  'Good news: no stale water sitting in a tank. The catch: every cup means one more step, so it is slower for a household that drinks several cups in a row. Keurig advises against distilled water.'),
 ('cup-sizes', 'What cup sizes can it brew, and will my mug fit?',
  'Any amount between 6 and 12 oz, because it brews the water you pour in. It fits travel mugs up to 7 inches tall once you remove the drip tray.',
  'The drip tray catches up to 8 oz of overflow, so empty it now and then. For a big 16 oz travel mug you would need two brews.'),
 ('pods', 'Which pods are compatible?',
  'K-Cup pods. To use your own ground coffee, Keurig says the K-Mini works with the My K-Cup reusable coffee filter (sold separately).',
  'Some owners report that certain universal reusable filters fit tightly in the K-Mini: check the filter’s listing for K-Mini compatibility before you order one.'),
 ('cleaning', 'How easy is it to clean?',
  'Day to day it is simple: wipe the outside, empty the drip tray, and remove the pod holder and funnel to rinse them. Keurig recommends a rinse pod weekly and descaling every 3 months, which takes about 45 minutes.',
  'If grounds end up in your cup, Keurig’s guide shows how to clear the entrance and exit needles with a straightened paper clip. Hard water means descaling more often.'),
 ('disadvantages', 'What are its disadvantages?',
  'One cup per fill, no strong-brew setting (the K-Mini Plus adds one), no built-in pod storage, and pods cost more per cup than ground coffee. In owner reviews, the most repeated complaints are about durability over time and coffee that tastes flat.',
  'Owner reviews are opinions, not lab tests, but when the same complaint repeats it is worth knowing before you buy. Regular descaling helps the brewer keep working well.'),
 ('vs-alternatives', 'How does it compare with the alternatives?',
  'K-Mini Plus: same idea, plus a Strong brew button and pod storage, for a higher price. A drip coffee maker with a carafe, like the OXO Brew 8-Cup in our coffee maker guide, is better for several cups at once. An espresso machine is the pick for lattes.',
  'Choose by how many cups your home drinks on a weekday: one or two points to a single-serve brewer like the K-Mini; four or more points to a drip machine.'),
 ('who-should-buy', 'Who should buy it?',
  'One person or a light coffee drinker, a small kitchen, a dorm room, an office desk or a guest room: anyone who wants a quick cup with no carafe to wash.',
  'The cord storage at the back and the narrow body also make it easy to put away or move between rooms.'),
 ('who-should-skip', 'Who should skip it?',
  'Skip it if you brew for two or more people every morning: each cup means pouring water, a new pod and waiting about 2 minutes for it to heat. Also skip it if you want strong, café-style coffee or the lowest cost per cup.',
  'For several cups, look at a drip coffee maker with a thermal carafe; for lattes and cappuccinos, an espresso machine. Both are in our coffee maker guide.'),
]
KM_SPECS = [('Width', 'Less than 5 in. (Keurig); about 4.5 in. (retailer specs)'), ('Brew size', '6 to 12 oz: it brews the water you pour in'), ('Water', 'Single-cup reservoir, filled for each brew'),
            ('Mug fit', 'Travel mugs up to 7 in. tall (drip tray removed)'), ('Pods', 'K-Cup pods; My K-Cup reusable filter compatible'), ('Auto off', 'After a brew, or after 5 minutes of inactivity'),
            ('Extras', 'Cord storage, high-altitude mode'), ('Care', 'Descale every 3 months (about 45 min)')]

def _km_page():
    toc = ''.join(f'<li><a href="#{a}"><u>{q}</u></a></li>' for a, q, _, _ in KM_Q)
    qs = ''.join(f'<section class="step" id="{a}"><div class="shead"><div><div class="n">{i + 1:02d}</div><h2 class="h3" style="font-size:28px">{q}</h2></div></div><p><b>Short answer:</b> {s}</p><p>{d}</p><div class="tip">👉 <a href="{KM_AFF}" target="_blank" rel="sponsored nofollow noopener"><u>Check the K-Mini’s current price and photos on Amazon</u></a></div></section>' for i, (a, q, s, d) in enumerate(KM_Q))
    specs = ''.join(f'<li><b>{k}:</b> {v}</li>' for k, v in KM_SPECS)
    card = f'''<article class="pick top"><span class="badge b1">ONE-CUP PICK</span><div class="phead"><h3 class="h4">Keurig K-Mini Single-Serve Coffee Maker</h3></div><div class="for">Best for: one person, small spaces</div><ul>{specs}</ul><a class="amz" href="{KM_AFF}" target="_blank" rel="sponsored nofollow noopener">See photos &amp; price on Amazon →</a><div class="price">Price and availability change often: check on Amazon</div></article>'''
    body = f'''<div class="crumb"><a href="/">Home</a> › <a href="/guides/coffee-maker/">Coffee makers</a> › Keurig K-Mini</div>
<section class="ghead"><div><div class="kick">Before you buy · Coffee</div><h1>Keurig K-Mini: <i>10 questions to answer before you buy</i></h1><p class="lead">Is it worth it, will it fit, what pods does it take, and who should skip it? Straight answers from Keurig’s official Use &amp; Care Guide and the most repeated owner feedback.</p><div class="by"><span>Updated November 2026</span><span>· 5 min read</span><span>· Specs from Keurig</span></div></div>{img('/assets/img/cf-breakfast-coffee.jpg', 'A cup of coffee on a breakfast table (illustration)', 'gimg', lazy=False)}</section>
<section class="verdict" id="picks"><h2 class="kick">Quick facts · Keurig K-Mini</h2><div class="picks" style="grid-template-columns:minmax(0,1fr)">{card}</div><p class="disc">As an Amazon Associate we earn from qualifying purchases, at no extra cost to you. Specs come from Keurig’s <a href="{KM_GUIDE}" target="_blank" rel="noopener"><u>official K-Mini Use &amp; Care Guide</u></a>; the width comes from Keurig and retailer listings. The photo on this page is a mood illustration, not the product: see the real product photos on Amazon.</p></section>
<div class="two"><div>{qs}<p style="margin:18px 0"><a href="/guides/coffee-maker/"><u>Not sure a pod machine is right for you? Read our full coffee maker guide (6 criteria + 3 picks) →</u></a></p></div>
<aside><div class="check"><h3>The 10 questions</h3><ol style="padding-left:20px;line-height:1.7">{toc}</ol></div></aside></div>'''
    schema = [
        {'@context': 'https://schema.org', '@type': 'Article', 'headline': 'Keurig K-Mini: 10 questions to answer before you buy', 'image': [SITE + '/assets/img/cf-breakfast-coffee.jpg'], 'datePublished': '2026-11-11', 'dateModified': '2026-11-11', 'author': ORG, 'publisher': ORG, 'mainEntityOfPage': SITE + KM_URL},
        {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': s}} for _, q, s, _ in KM_Q]},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'}, {'@type': 'ListItem', 'position': 2, 'name': 'Coffee makers', 'item': SITE + '/guides/coffee-maker/'}, {'@type': 'ListItem', 'position': 3, 'name': 'Keurig K-Mini', 'item': SITE + KM_URL}]},
    ]
    write(KM_URL.strip('/') + '/index.html', page('Keurig K-Mini Review: 10 Questions to Answer Before You Buy (2026)',
          'Is the Keurig K-Mini worth it? Width, water refills, cup sizes, pods, cleaning, disadvantages, alternatives, and who should buy or skip it, from Keurig’s official guide.',
          KM_URL, body, image='/assets/img/cf-breakfast-coffee.jpg', schema=schema, preload_img='/assets/img/cf-breakfast-coffee.jpg'))
    EXTRA_PAGES.append((KM_URL, '0.8'))
    # lien depuis le guide cafetière
    f = 'guides/coffee-maker/index.html'
    s = open(f).read()
    if 'id="deep"' not in s:
        write(f, s.replace('<div class="two">', f'<section class="sec" id="deep" style="padding-top:0"><h2>Before you buy a specific model</h2><div class="cats"><a class="cat" style="padding:14px 18px" href="{KM_URL}">Keurig K-Mini: 10 questions answered</a></div></section><div class="two">', 1))

_km_page()
