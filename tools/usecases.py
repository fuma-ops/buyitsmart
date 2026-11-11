# Pages « Best X for Y » (SEO programmatique) : générées à partir des produits déjà vérifiés
# dans les guides principaux (PICKS, AF_PICKS). Aucune caractéristique nouvelle n'est inventée :
# chaque page reprend les points vérifiés du produit et ajoute les critères propres au besoin.
# Exécuté depuis build.py (exec), qui fournit page(), img(), PICKS, AF_PICKS, SITE, TAG, ORG, UPDATED.

def _pick_by(name, src):
    return next(p for p in src if p[2] == name)

def _card(p, why):
    b, bc, n, f, pts, u, im, alt, top = p
    return f'''<article class="pick"><span class="badge {bc}">{b}</span><div class="phead"><a class="pimg" href="{u}" target="_blank" rel="sponsored nofollow noopener">{img(im, alt, w=800, h=600)}</a><h3 class="h4">{n}</h3></div><div class="for">Why it fits: {why}</div><ul>{''.join(f'<li>{x}</li>' for x in pts)}</ul><a class="amz" href="{u}" target="_blank" rel="sponsored nofollow noopener">See photos &amp; price on Amazon →</a><div class="price">Price and availability change often: check on Amazon</div></article>'''

RV = 'Roborock Q10 S5+'; EU = 'eufy HydroJet robot vacuum &amp; mop'; SA = 'Roborock Saros 10R'
CO = 'COSORI Pro LE 5-Qt Air Fryer'; NI = 'Ninja Crispi 4-in-1 Glass Air Fryer'; BR = 'Breville Smart Oven Air Fryer Pro'

USE = {
 'robot-vacuum': dict(label='Robot vacuums', crumb='Cleaning', main='/guides/robot-vacuum/', src=PICKS, hero='/assets/img/robot-vacuum.jpg', noun='robot vacuum', items=[
  dict(slug='for-pet-hair', need='pet hair', title='Best robot vacuum for pet hair (2026): what matters + our picks',
       lead='For pet hair, three things matter more than raw suction: brushes that don’t tangle, obstacle avoidance that steers around pet messes, and a self-emptying base that swallows all that fur for you.',
       picks=[(EU, 'zero-tangle brushes for pet hair and AI obstacle avoidance for pet messes'), (SA, 'top-tier navigation and mopping for big homes with pets')],
       crit=[('Brushes that don’t tangle', 'Classic bristle brushes wrap pet hair and need cutting every week. Rubber or “anti-tangle” rollers keep working on their own.'),
             ('Real obstacle avoidance', 'Bowls, toys and accidents: only robots with AI or camera-based obstacle avoidance really try to steer around them. Basic models only sense walls and stairs.'),
             ('A self-emptying base', 'Fur fills a small bin in one run. A base that empties the robot into a bag means you deal with it every few weeks, not every day.'),
             ('Suction where the hair is', 'Hair hides in rugs. Higher suction with automatic carpet boost helps; on hard floors, mid-range suction is enough.')],
       faq=[('Do robot vacuums get clogged with pet hair?', 'Bristle brushes often wrap long pet hair. Rubber or anti-tangle brushes reduce this a lot, and a self-emptying base keeps the bin from filling up mid-run.'),
            ('Can a robot vacuum avoid pet poop?', 'Only models with AI or camera-based obstacle avoidance try to recognize it, and none is perfect. If you have a puppy or a sick pet, check the floor before a scheduled run.'),
            ('How often should a robot vacuum run with pets?', 'Many owners run it daily during shedding season. A schedule plus a self-emptying base keeps fur under control without extra work.')]),
  dict(slug='for-long-hair', need='long hair', title='Best robot vacuum for long hair (2026): no more cutting hair off the brush',
       lead='Long hair is the number one reason people give up on their robot vacuum: it wraps around the brush. The fix is simple: choose dual or anti-tangle rubber brushes.',
       picks=[(RV, 'dual anti-tangle brushes, great with long hair, at a budget price'), (EU, 'zero-tangle brushes and a self-cleaning roller mop')],
       crit=[('Dual or anti-tangle rubber brushes', 'They let hair slide off instead of wrapping around. It is the single most important feature for long hair.'),
             ('Check the side brush too', 'Hair can also wrap around the small spinning side brush: read reviews from people with long hair.'),
             ('A self-emptying base', 'Hair and dust go into a bag in the dock, so you are not pulling hair out of a small bin every day.'),
             ('Easy brush removal', 'Even the best brushes need a quick clean now and then: tool-free removal makes it a 30-second job.')],
       faq=[('Which robot vacuum brushes are best for long hair?', 'Dual rubber or anti-tangle brushes. Classic bristle brushes catch and wrap long hair much more often.'),
            ('How do I get hair off a robot vacuum brush?', 'Remove the brush, then cut or pull the hair along the groove that many brushes have for this. Anti-tangle designs need this far less often.')]),
  dict(slug='for-hardwood-floors', need='hardwood floors', title='Best robot vacuum for hardwood floors (2026): what matters + our pick',
       lead='On hardwood and tile you don’t need the strongest suction: you need neat mapping, a gentle brush and, if it mops, careful control of the water.',
       picks=[(RV, 'LiDAR mapping, anti-tangle brushes and a mop that lifts on carpets, made for hard floors')],
       crit=[('Mid-range suction is enough', 'Hard floors don’t trap dirt like carpet. Spend on navigation and brushes rather than the highest Pa number.'),
             ('Neat rows with LiDAR', 'LiDAR mapping cleans in straight lines and doesn’t miss spots along walls and under tables.'),
             ('Mop with little water', 'Wood doesn’t like standing water: a robot mop that dampens rather than soaks is safer. Follow your floor maker’s advice.'),
             ('A mop that lifts on rugs', 'If you have rugs on your hardwood, the mop should lift or the robot should avoid them.')],
       faq=[('Will a robot vacuum scratch hardwood floors?', 'Normally not: wheels and brushes are designed for hard floors. Keep the wheels and brush free of grit, which is what can mark a floor.'),
            ('Can I use a robot mop on hardwood?', 'Yes on sealed hardwood, with little water. Check your floor maker’s cleaning advice first.')]),
  dict(slug='for-small-apartment', need='small apartments', title='Best robot vacuum for a small apartment (2026): our pick',
       lead='In a small apartment, the best robot vacuum is the one you forget about: it maps your rooms, avoids the no-go spots, fits under the sofa and has a dock that doesn’t take over the hallway.',
       picks=[(RV, 'LiDAR room mapping, self-emptying dock and a mop that lifts on carpets, at a budget price')],
       crit=[('Room mapping and no-go zones', 'Keep the robot away from the pet bowl, the cables behind the TV or the kids’ corner.'),
             ('Check the dock footprint', 'Self-emptying and mopping docks need space around them: measure the spot before you buy.'),
             ('Height under your furniture', 'Measure the gap under your sofa and bed and compare it with the robot’s height on the product page.'),
             ('Noise matters in small spaces', 'Schedule runs while you are out, and check quiet modes in reviews.')],
       faq=[('Is a robot vacuum worth it for a small apartment?', 'Yes for most people: in a small space it can run every day in a few minutes, and a self-emptying dock means almost no maintenance.'),
            ('Do I need a mopping robot in a small apartment?', 'It is a bonus for kitchens and bathrooms with hard floors. Choose a mop that lifts on carpets if you have rugs.')]),
  dict(slug='for-large-home', need='large homes', title='Best robot vacuum for a large home (2026): what matters + our picks',
       lead='In a large home, you want a robot that runs on its own for days: precise navigation, an all-in-one station, and the ability to cross door sills and rug edges.',
       picks=[(SA, 'StarSight 3D navigation, threshold climbing up to 4 cm and smart re-mopping'), (EU, 'HydroJet self-cleaning roller mop and AI obstacle avoidance')],
       crit=[('Navigation you can trust', 'Large spaces need accurate maps: LiDAR or 3D navigation, with room-by-room control in the app.'),
             ('An all-in-one station', 'Self-emptying, mop washing and drying: the less you touch it, the more it runs.'),
             ('Thresholds and rug edges', 'Check the maximum height it can climb so it reaches every room.'),
             ('Several floors?', 'If you have stairs, check on the product page how many floor maps it saves.')],
       faq=[('How big a home can a robot vacuum clean?', 'It depends on battery life and whether it can recharge and resume. Check both on the product page for large homes.'),
            ('Can one robot vacuum do several floors?', 'Many models save several maps, but you still have to carry the robot upstairs. Check the number of saved maps.')]),
  dict(slug='for-mopping', need='vacuuming and mopping', title='Best robot vacuum and mop combo (2026): what matters + our picks',
       lead='A robot vacuum and mop is only worth it if the mop stays clean and stays off your rugs. Look at how it mops, how it cleans the mop, and what it does on carpet.',
       picks=[(EU, 'HydroJet roller mop that cleans itself while mopping'), (SA, 'detects dirty areas and re-mops them, with a premium station')],
       crit=[('How it mops', 'Vibrating pads, spinning pads and roller mops don’t clean the same way: rollers that rinse themselves avoid spreading dirty water.'),
             ('A mop that lifts on carpet', 'A mop that stays down will wet your rugs. Choose one that lifts its mop or can avoid carpets.'),
             ('Washing and drying', 'A station that washes and dries the mop reduces odors and maintenance.'),
             ('Check the running costs', 'Mop pads, filters and cleaning solution: check their price and availability before you buy.')],
       faq=[('Do robot vacuum and mop combos really clean?', 'They are great for daily dust and light dirt on hard floors. Sticky stains still need a manual mop now and then.'),
            ('Will a mopping robot wet my rugs?', 'Not if it lifts its mop on carpet or if you set no-mop zones. Check this before you buy.')]),
  dict(slug='for-allergies', need='allergies', title='Best robot vacuum for allergies (2026): what matters + our picks',
       lead='For allergies, the goal is less dust in the air and less contact with it. Daily runs and a self-emptying base that keeps dust sealed in a bag make the biggest difference.',
       picks=[(RV, 'self-emptying dock: you empty a bag every few weeks, not a dusty bin every day'), (EU, 'zero-tangle brushes and a self-cleaning roller mop for fine dust on hard floors')],
       crit=[('Self-emptying into a bag', 'You avoid the cloud of dust that comes out of a small bin, since it stays in the bag in the dock.'),
             ('Check the filter', 'Look for a fine filter on the product page and the price of replacements.'),
             ('Run it often', 'A daily schedule keeps dust and dander from building up between deep cleans.'),
             ('Mopping for fine dust', 'On hard floors, a damp mop picks up the fine dust a vacuum leaves behind.')],
       faq=[('Do robot vacuums help with allergies?', 'They help by removing dust and dander more often. A self-emptying base also limits your contact with dust. They don’t replace an air purifier or medical advice.'),
            ('Is a self-emptying robot vacuum better for allergies?', 'Yes, because you empty a sealed bag every few weeks instead of a small bin every day.')]),
 ]),
 'air-fryer': dict(label='Air fryers', crumb='Kitchen', main='/guides/air-fryer/', src=AF_PICKS, hero='/assets/img/air-fryer.jpg', noun='air fryer', items=[
  dict(slug='for-family-of-4', need='a family of 4', title='Best air fryer for a family of 4 (2026): size + our picks',
       lead='For a family of four, size is everything: food must fit in one layer to get crispy. Count about 5 quarts for everyday meals, or an air fryer oven to cook a whole tray at once.',
       picks=[(CO, '5-quart square basket, sized for 2 to 4 people'), (BR, 'about 1 cu ft: fits a 9×13" pan, made for families')],
       crit=[('5 quarts minimum', 'Under that, you will cook in two batches. A square basket gives more flat space than a round one of the same size.'),
             ('Dual drawer or oven?', 'A dual drawer cooks a main and a side together; an oven-style air fryer bakes and roasts on flat trays.'),
             ('Dishwasher-safe parts', 'With family meals every day, easy cleaning decides if you keep using it.'),
             ('Leave space behind it', 'Hot air comes out of the back: measure your counter.')],
       faq=[('What size air fryer for a family of 4?', 'About 5 quarts for everyday cooking, or 6 quarts and up, or an air fryer oven, if you batch cook or cook a whole chicken.'),
            ('Is a dual basket air fryer good for a family?', 'Yes if you often cook a main and a side at the same time. Otherwise a single large basket is simpler to clean.')]),
  dict(slug='for-one-or-two-people', need='one or two people', title='Best air fryer for 1 or 2 people (2026): our picks',
       lead='For one or two people, a big air fryer just takes counter space. A 3 to 5-quart model heats fast, cooks crispy, and is easier to clean.',
       picks=[(NI, 'made for 1 to 2 people: cook, serve and store in the same glass container'), (CO, '5 quarts when you cook for two with leftovers')],
       crit=[('2 to 5 quarts', 'About 2 to 3 quarts for one person, 4 to 5 for two people with leftovers or meal prep.'),
             ('Counter space', 'Measure where it will live, with space behind for the hot air.'),
             ('Easy cleaning', 'You will use it daily: dishwasher-safe parts make the difference.')],
       faq=[('What size air fryer for 2 people?', 'About 4 to 5 quarts if you want leftovers or meal prep; 3 quarts is enough for small portions.'),
            ('Is a small air fryer faster?', 'Smaller baskets usually heat up quickly, which is great for quick meals for one or two.')]),
  dict(slug='non-toxic', need='non-toxic, PFAS-free cooking', title='Best non-toxic air fryer (2026): glass, ceramic or steel + our pick',
       lead='If you want to avoid traditional nonstick coatings, look at what actually touches your food: glass, stainless steel or ceramic, and read the brand’s PFAS-free claim carefully.',
       picks=[(NI, 'cooks in glass containers that Ninja markets as PFAS-free (the crisper plate has a ceramic nonstick coating)')],
       crit=[('Check every part that touches food', 'Basket, crisper plate, inner walls: a “PFAS-free” label may cover only some of them.'),
             ('Glass, steel or ceramic', 'Glass and stainless steel have no coating; ceramic is a coating but not a traditional PTFE one.'),
             ('Care for any coating', 'Never use metal utensils or scouring pads, and replace a basket if the coating peels.')],
       faq=[('Are air fryers toxic?', 'Nonstick coatings are generally considered safe when they are not scratched or overheated. If you prefer to avoid them, choose glass, stainless steel or ceramic surfaces.'),
            ('What does PFAS-free mean on an air fryer?', 'It is the brand’s own claim about the materials used. Check which parts it covers on the product page.')]),
  dict(slug='for-meal-prep', need='meal prep', title='Best air fryer for meal prep (2026): our pick',
       lead='For meal prep, the best air fryer is the one that saves you dishes: cook, serve and store in the same container, and see the food brown without opening.',
       picks=[(NI, 'cook, serve and store in the same glass container, and watch it brown through the glass')],
       crit=[('Containers you can store', 'Glass containers that go from air fryer to fridge save time and dishes.'),
             ('See-through cooking', 'A window or glass container lets you check browning without letting heat out.'),
             ('Capacity for your batches', 'Small models are perfect for 1 to 2 people; bigger batches need 5 quarts or more.')],
       faq=[('Can you meal prep with an air fryer?', 'Yes: roasted vegetables, chicken and fish cook in minutes. Containers you can also store in make it even easier.')]),
  dict(slug='toaster-oven', need='replacing the toaster and the oven', title='Best air fryer toaster oven (2026): when it’s worth it + our pick',
       lead='An air fryer toaster oven is bigger and slower to preheat than a basket air fryer, but it bakes, toasts and roasts on flat trays, and can replace two or three appliances.',
       picks=[(BR, 'about 1 cu ft, 13 cooking functions, stainless steel body')],
       crit=[('Capacity in pans and slices', 'Check what fits: a 9×13" pan, slices of bread, a whole chicken.'),
             ('Basket vs oven', 'For the crispiest fries, a basket is faster. For trays, toast and baking, the oven wins.'),
             ('Counter space and heat', 'Ovens are wide: measure your counter and leave space around for heat.')],
       faq=[('Air fryer or air fryer toaster oven?', 'A basket air fryer is faster and crispier for fries and wings. An air fryer oven is bigger and can bake, toast and roast, but preheats more slowly.')]),
 ]),
}

EXTRA_PAGES = []
def _usecase_page(cat_key, cat, it):
    path = f'{cat["main"]}{it["slug"]}/'
    picks = [(_pick_by(n, cat['src']), why) for n, why in it['picks']]
    cards = ''.join(_card(p, why) for p, why in picks)
    crit = ''.join(f'<section class="step"><div class="shead"><div><div class="n">0{i + 1}</div><h3>{h}</h3></div></div><p>{p}</p></section>' for i, (h, p) in enumerate(it['crit']))
    faq = '<section class="faq"><h2>FAQ</h2>' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in it['faq']) + '</section>'
    sib = ''.join(f'<li><a href="{cat["main"]}{o["slug"]}/"><u>Best {cat["noun"]} for {o["need"]}</u></a></li>' for o in cat['items'] if o['slug'] != it['slug'])
    name = it['title'].split(' (')[0]
    body = f'''<div class="crumb"><a href="/">Home</a> › <a href="{cat["main"]}">{cat["crumb"]}</a> › <a href="{cat["main"]}">{cat["label"]}</a> › For {it["need"]}</div>
<section class="ghead"><div><div class="kick">Smart buying guide · {cat["label"]}</div><h1>{it["title"].split(":")[0]}: <i>{it["title"].split(": ", 1)[1]}</i></h1><p class="lead">{it["lead"]}</p><div class="by"><span>Updated November 2026</span><span>· 3 min read</span></div></div>{img(cat["hero"], name, "gimg", lazy=False)}</section>
<section class="verdict" id="picks"><h2 class="kick">Quick answer · Our pick{"s" if len(picks) > 1 else ""} for {it["need"]}</h2><div class="picks">{cards}</div><p class="disc">As an Amazon Associate we earn from qualifying purchases, at no extra cost to you. These picks come from our full <a href="{cat["main"]}"><u>{cat["noun"]} buying guide</u></a>, based on our criteria, published expert tests and brand specs. Product photos are illustrations: see the real photos on Amazon.</p></section>
<div class="two"><div><h2 style="margin-bottom:24px">What matters most for {it["need"]}</h2>{crit}<p style="margin:18px 0"><a href="{cat["main"]}#checklist"><u>All 6 criteria and the free checklist in our full {cat["noun"]} guide →</u></a></p>{faq}</div>
<aside><div class="check"><h3>More {cat["noun"]} guides</h3><ul style="list-style:none;padding:0;line-height:1.9">{sib}<li><a href="{cat["main"]}"><u>Full {cat["noun"]} buying guide</u></a></li></ul></div></aside></div>'''
    schema = [
        {'@context': 'https://schema.org', '@type': 'Article', 'headline': it['title'], 'image': [SITE + cat['hero']], 'datePublished': '2026-11-11', 'dateModified': '2026-11-11', 'author': ORG, 'publisher': ORG, 'mainEntityOfPage': SITE + path},
        {'@context': 'https://schema.org', '@type': 'ItemList', 'name': name, 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': p[2].replace('&amp;', '&'), 'url': p[5]} for i, (p, _) in enumerate(picks)]},
        {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in it['faq']]},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'}, {'@type': 'ListItem', 'position': 2, 'name': cat['label'], 'item': SITE + cat['main']}, {'@type': 'ListItem', 'position': 3, 'name': f'For {it["need"]}', 'item': SITE + path}]},
    ]
    desc = (it['lead'][:150].rsplit(' ', 1)[0] + '…') if len(it['lead']) > 155 else it['lead']
    title_tag = it['title'].replace('&amp;', '&')
    write(path.strip('/') + '/index.html', page(title_tag, desc.replace('"', '&quot;'), path, body, image=cat['hero'], schema=schema, preload_img=cat['hero']))
    EXTRA_PAGES.append((path, '0.7'))

for k, cat in USE.items():
    for it in cat['items']:
        _usecase_page(k, cat, it)

# ---------- Calculateur de taille de friteuse à air ----------
CALC_PATH = '/guides/air-fryer/size-calculator/'
calc = f'''<div class="crumb"><a href="/">Home</a> › <a href="/guides/air-fryer/">Kitchen</a> › Air fryer size calculator</div>
<section class="ghead"><div><div class="kick">Free tool · Air fryers</div><h1>What size air fryer do I need? <i>Free calculator</i></h1><p class="lead">Answer two questions and get the air fryer size that cooks your food in one layer, the only way to get it crispy.</p></div>{img('/assets/img/af-size-small-medium-large.jpg', 'Small, medium and large air fryers side by side', 'gimg', lazy=False)}</section>
<section class="verdict"><div class="check" style="max-width:640px"><h3>Your household</h3>
<p><label>How many people do you usually cook for?<br><select id="ppl" style="font-size:18px;padding:10px;border-radius:12px;margin-top:8px"><option value="1">1 person</option><option value="2" selected>2 people</option><option value="3">3 people</option><option value="4">4 people</option><option value="5">5 people</option><option value="6">6 or more</option></select></label></p>
<p><label><input type="checkbox" id="batch"> I batch cook, meal prep or cook whole chickens</label></p>
<div id="res" style="margin-top:18px;padding:18px;border-radius:16px;background:#ecfdf5;color:#065f46;font-size:20px"></div></div></section>
<div class="prose"><h2>How we calculate it</h2><p>Food has to sit in one layer for the hot air to crisp it. Our rule of thumb: about <b>2 to 3 quarts for one person</b>, <b>4 to 5 quarts for two to four people</b>, and <b>6 quarts or more, or an air fryer oven, for families</b> and batch cooking. At the same capacity, a square basket gives more flat space than a round one.</p>
<p>Next step: <a href="/guides/air-fryer/"><u>how to choose an air fryer (6 criteria + 3 picks)</u></a> · <a href="/guides/air-fryer/for-family-of-4/"><u>best air fryer for a family of 4</u></a> · <a href="/guides/air-fryer/for-one-or-two-people/"><u>best air fryer for 1 or 2 people</u></a></p></div>
<script>(()=>{{const p=document.getElementById('ppl'),b=document.getElementById('batch'),r=document.getElementById('res');const up=()=>{{const n=+p.value,x=b.checked;let s,l;if(n<=1){{s=x?'4 to 5 quarts':'2 to 3 quarts';l=x?'/guides/air-fryer/for-meal-prep/':'/guides/air-fryer/for-one-or-two-people/'}}else if(n<=4){{s=x||n==4?'5 to 6 quarts':'4 to 5 quarts';l=n>=4?'/guides/air-fryer/for-family-of-4/':'/guides/air-fryer/for-one-or-two-people/'}}else{{s='6 quarts or more, or an air fryer oven';l='/guides/air-fryer/toaster-oven/'}}r.innerHTML='👉 You need: <b>'+s+'</b><br><a style="color:#065f46" href="'+l+'"><u>See our pick for you →</u></a>'}};p.onchange=up;b.onchange=up;up()}})()</script>'''
write(CALC_PATH.strip('/') + '/index.html', page('What Size Air Fryer Do I Need? Free Air Fryer Size Calculator (2026)',
      'Free air fryer size calculator: how many quarts you need for 1, 2, 4 or 6 people, plus our pick for your household.', CALC_PATH, calc, image='/assets/img/af-size-small-medium-large.jpg',
      schema=[{'@context': 'https://schema.org', '@type': 'WebApplication', 'name': 'Air fryer size calculator', 'url': SITE + CALC_PATH, 'applicationCategory': 'UtilitiesApplication', 'isAccessibleForFree': True, 'publisher': ORG}]))
EXTRA_PAGES.append((CALC_PATH, '0.7'))

# ---------- Liens « par besoin » dans les guides principaux et la page des guides ----------
def _inject(file, block, marker='<div class="two">'):
    s = open(file).read()
    if 'id="byneed"' in s: return
    write(file, s.replace(marker, block + marker, 1))
for k, cat in USE.items():
    links = ''.join(f'<a class="cat" style="padding:14px 18px" href="{cat["main"]}{it["slug"]}/">For {it["need"]}</a>' for it in cat['items'])
    if k == 'air-fryer': links += f'<a class="cat" style="padding:14px 18px" href="{CALC_PATH}">📏 Size calculator</a>'
    _inject(cat['main'].strip('/') + '/index.html', f'<section class="sec" id="byneed" style="padding-top:0"><h2>Find the right {cat["noun"]} for your home</h2><div class="cats">{links}</div></section>')
hub_links = ''.join(f'<li><a href="{cat["main"]}{it["slug"]}/"><u>Best {cat["noun"]} for {it["need"]}</u></a></li>' for cat in USE.values() for it in cat['items']) + f'<li><a href="{CALC_PATH}"><u>Air fryer size calculator</u></a></li>'
s = open('guides/index.html').read()
if 'id="byneed"' not in s:
    write('guides/index.html', s.replace('</section>', f'<section class="sec" id="byneed"><h2>Find the right one for your needs</h2><ul style="line-height:2">{hub_links}</ul></section></section>', 1))
