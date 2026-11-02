"""Génère les pages HTML du site (python3 tools/build.py depuis la racine du dépôt)."""
import json
import os

SITE = 'https://buyitsmart.fumaops.com'
TAG = 'bloomshop09-20'
UPDATED = '2026-11-02'

NAV = '''<header class="wrap"><nav><a class="logo" href="/" aria-label="Buy It Smart home">Buy it <i>smart</i></a><div class="links"><a href="/#rooms">Kitchen</a><a href="/guides/robot-vacuum/">Cleaning</a><a href="/#rooms">Coffee</a><a href="/#rooms">Bedroom</a><a href="/#rooms">Storage</a><a href="/about/">How we choose</a></div><a class="pill" href="/guides/robot-vacuum/#checklist">✓ Free checklists</a></nav></header>'''
FOOT = '''<footer><div class="wrap"><b class="flogo">Buy it <i>smart</i></b><br>Smart buying guides for your home. What really matters before you buy, so you only buy it once.<br>As an Amazon Associate we earn from qualifying purchases. This never changes our criteria.<br><a href="/guides/robot-vacuum/">Best robot vacuum guide</a> · <a href="/about/">About &amp; how we choose</a> · <a href="/privacy/">Privacy</a> · Instagram <a href="https://www.instagram.com/buyitsmartguides/" rel="noopener" target="_blank">@buyitsmartguides</a><br>© 2026 Buy It Smart · Illustration photos: Pixabay</div></footer>'''


def page(title, desc, path, body, image='/assets/img/og.jpg', schema=None, preload_img=None):
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in (schema or []))
    pre = f'<link rel="preload" as="image" href="{preload_img}">' if preload_img else ''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><meta name="description" content="{desc}"><meta name="robots" content="index,follow,max-image-preview:large"><link rel="canonical" href="{SITE}{path}"><meta property="og:site_name" content="Buy It Smart"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{SITE}{path}"><meta property="og:image" content="{SITE}{image}"><meta property="og:type" content="{'article' if path.startswith('/guides/') else 'website'}"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/favicon.png"><link rel="preload" href="/assets/fonts/PlayfairDisplay-900-normal.woff2" as="font" type="font/woff2" crossorigin>{pre}<link rel="stylesheet" href="/assets/style.css">{ld}</head><body>{NAV}<main class="wrap">{body}</main>{FOOT}</body></html>'''


def img(src, alt, cls='', lazy=True, w=1200, h=800):
    extra = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return f'<img class="{cls}" src="{src}" alt="{alt}" width="{w}" height="{h}"{extra}>'


def write(path, html):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w') as f:
        f.write(html)


ORG = {'@type': 'Organization', 'name': 'Buy It Smart', 'url': SITE, 'logo': SITE + '/assets/img/logo-512.png', 'sameAs': ['https://www.instagram.com/buyitsmartguides/']}

# ---------- Accueil ----------
home = f'''<section class="hero"><div><div class="kick">Smart buying guides for your home</div><h1>Buy it <i>smart.</i><br>Buy it once.</h1><p class="lead">Home buying guides that tell you what really matters before you buy: clear criteria, honest picks for every budget, and checklists you can save.</p>
<form class="search" id="s" role="search"><input id="q" placeholder="What are you shopping for? Robot vacuum, air fryer…" aria-label="Search a buying guide"><button>Find the guide</button></form></div>
<div class="mosaic"><a href="/guides/robot-vacuum/">{img('/assets/img/robot-vacuum.jpg', 'Robot vacuum with LiDAR sensor cleaning a carpet', lazy=False)}<span class="tag">✓ Cleaning</span></a><div>{img('/assets/img/air-fryer.jpg', 'Air fryer with fries on a kitchen counter')}<span class="tag">✓ Kitchen</span></div><div>{img('/assets/img/coffee.jpg', 'Espresso machine in a cozy kitchen')}<span class="tag">✓ Coffee</span></div></div></section>
<div class="trust"><span><b>No hype.</b> Criteria first, products second</span><span><b>Every budget.</b> Small, medium, premium</span><span><b>Real data.</b> Prices &amp; ratings on Amazon</span></div>
<section class="sec" id="rooms"><h2>Shop smart, room by room</h2><div class="cats">
<a class="cat" href="/#guides">{img('/assets/img/air-fryer.jpg', 'Kitchen appliances buying guides', w=300, h=200)}Kitchen</a><a class="cat" href="/guides/robot-vacuum/">{img('/assets/img/robot-top-wood.jpg', 'Robot vacuum on a wooden floor', w=300, h=200)}Cleaning</a><a class="cat" href="/#guides">{img('/assets/img/coffee.jpg', 'Coffee machines buying guides', w=300, h=200)}Coffee</a><a class="cat" href="/#guides">{img('/assets/img/bedroom.jpg', 'Bedding and bedroom buying guides', w=300, h=200)}Bedroom</a><a class="cat" href="/#guides">{img('/assets/img/storage-jars.jpg', 'Kitchen storage jars', w=300, h=200)}Storage</a><a class="cat" href="/#guides">{img('/assets/img/blender.jpg', 'Blender and small appliances', w=300, h=200)}Appliances</a></div></section>
<section class="sec" id="guides" style="padding-top:0"><h2>Latest buying guides</h2><div class="guides">
<a class="card" href="/guides/robot-vacuum/">{img('/assets/img/robot-vacuum.jpg', 'Best robot vacuum 2026 buying guide', 'im')}<div class="bd"><div class="kick">Cleaning</div><h3>Best robot vacuum 2026: the 6 things that matter</h3><p>Navigation, suction, obstacle avoidance… and 3 picks for every budget.</p><div class="meta"><span>7 min read</span><span>· Checklist inside</span></div></div></a>
<div class="card"><span class="soon">Coming soon</span>{img('/assets/img/air-fryer.jpg', 'Healthy air fryer guide', 'im')}<div class="bd"><div class="kick">Kitchen</div><h3>The healthy air fryer guide: size, coating, cleaning</h3><p>Stainless or ceramic basket, single or dual drawer, what to skip.</p><div class="meta"><span>6 min read</span><span>· Checklist inside</span></div></div></div>
<div class="card"><span class="soon">Coming soon</span>{img('/assets/img/pantry.jpg', 'Organized pantry with jars and baskets', 'im')}<div class="bd"><div class="kick">Storage</div><h3>Pantry reset: the only 2 things you need</h3><p>Airtight jars and baskets: how to pick the right ones.</p><div class="meta"><span>4 min read</span><span>· Checklist inside</span></div></div></div></div></section>
<section class="sec" style="padding-top:0"><h2>How we choose</h2><div class="how"><div><b>1. Criteria first</b>We explain what actually changes your daily life with a product, before naming any model.</div><div><b>2. Expert tests &amp; reviews</b>We cross-check published expert tests and recurring buyer complaints, not just the stars.</div><div><b>3. One pick per budget</b>Small, medium, premium. Always check the current price on Amazon.</div></div></section>
<script>document.getElementById('s').addEventListener('submit',e=>{{e.preventDefault();const q=document.getElementById('q').value.trim();if(!q)return;if(/robot|vacuum|roomba|aspir/i.test(q)){{location.href='/guides/robot-vacuum/';return}}window.open('https://www.amazon.com/s?k='+encodeURIComponent(q)+'&tag={TAG}','_blank','noopener')}})</script>'''
write('index.html', page('Buy It Smart – Home buying guides: what matters before you buy',
                         'Smart home buying guides: what really matters before you buy a robot vacuum, air fryer or coffee machine, with honest picks for every budget and free checklists.',
                         '/', home, schema=[{'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'Buy It Smart', 'url': SITE + '/', 'publisher': ORG}], preload_img='/assets/img/robot-vacuum.jpg'))

# ---------- Guide robot aspirateur ----------
PICKS = [
    ('BEST BUDGET', 'b1', 'Roborock Q10 S5+', 'Apartments, hard floors and long hair, on a budget',
     ['LiDAR navigation and room mapping', 'Dual anti-tangle brushes (great with long hair)', 'Self-emptying dock + mop that lifts on carpets', 'Basic obstacle avoidance: keep floors clear'],
     'https://link.amazon/B0ceuLyPy', '/assets/img/robot-top-wood.jpg', 'Budget robot vacuum with LiDAR on a wooden floor (illustration)', ''),
    ('BEST OVERALL', 'b2', 'eufy HydroJet robot vacuum &amp; mop', 'Busy homes, pets and mixed floors',
     ['HydroJet roller mop that cleans itself while mopping', 'Zero-tangle brushes for pet and long hair', 'AI obstacle avoidance (cables, socks, pet mess)', 'See the product page for dock details'],
     'https://link.amazon/B0fuQInGd', '/assets/img/robot-vacuum.jpg', 'Robot vacuum and mop cleaning a carpet (illustration)', ' top'),
    ('PREMIUM', 'b3', 'Roborock Saros 10R', 'Large homes that want it all automated',
     ['StarSight 3D navigation + RGB camera', 'Climbs thresholds up to 4 cm (AdaptiLift chassis)', 'Detects dirty areas and re-mops them', 'Premium price: compare with current deals'],
     f'https://www.amazon.com/dp/B0DHCJ571Z?tag={TAG}', '/assets/img/robot-tile.jpg', 'Slim premium robot vacuum on a tiled floor (illustration)', ''),
]
cards = ''.join(f'''<article class="pick{top}"><span class="badge {bc}">{b}</span><a class="pimg" href="{u}" target="_blank" rel="sponsored nofollow noopener">{img(im, alt, w=600, h=400)}<span>Illustration · real photos on Amazon</span></a><h3 class="h4">{n}</h3><div class="for">Best for: {f}</div><ul>{''.join(f'<li>{x}</li>' for x in pts)}</ul><a class="amz" href="{u}" target="_blank" rel="sponsored nofollow noopener">See photos &amp; price on Amazon →</a><div class="price">Price and availability change often: check on Amazon</div></article>''' for b, bc, n, f, pts, u, im, alt, top in PICKS)

STEPS = [
    ('Navigation is the real difference', 'LiDAR (the small tower on top) maps your home and cleans in neat rows, even in the dark. Camera navigation is smart too but needs light. Random “bump &amp; go” models are cheaper but miss spots and take longer.', 'Want no-go zones (kids’ toys, pet bowls)? You need mapping: LiDAR or camera.', '/assets/img/robot-vacuum.jpg', 'LiDAR sensor on top of a robot vacuum'),
    ('Match suction to your floors', 'A higher suction number (in Pa) isn’t always worth paying for. Mostly hardwood or tile? Mid-range suction is enough. Carpets or pet hair? Go higher and look for automatic carpet boost.', 'Long hair at home? Choose rubber or “anti-tangle” brushes: no more cutting hair off the brush every week.', '/assets/img/carpet.jpg', 'Vacuum cleaning a carpet'),
    ('Obstacle avoidance', 'Cables, socks, kids’ toys, pet accidents… Basic models only sense walls and stairs. If your floor isn’t always clear, look for AI or camera-based obstacle avoidance.', 'Read reviews from pet owners: they tell the truth about this feature.', '/assets/img/dog-bed.jpg', 'Dog resting at home: pets need a robot vacuum with obstacle avoidance'),
    ('Will it actually fit?', 'Measure the space under your sofa and bed, then compare it with the robot’s height. Check the maximum threshold it can climb: door sills, rug edges.', 'Docking stations need free space around them: check the dimensions before you buy.', '/assets/img/robot-tile.jpg', 'Low-profile robot vacuum on a tiled floor'),
    ('A self-emptying base', 'You empty a bag every few weeks instead of a small bin every day. A real plus if someone at home has allergies, since dust stays sealed in the bag.', 'Check the price and availability of replacement bags.', '/assets/img/robot-top-wood.jpg', 'Robot vacuum seen from above on a wooden floor'),
    ('Mopping? Read this first', 'A mop that stays down will wet your rugs. Choose a robot vacuum and mop that lifts its mop on carpets, or that can be set to avoid them.', 'Washing and drying stations reduce odors and maintenance.', '/assets/img/robot-vacuum.jpg', 'Robot vacuum and mop on a rug'),
]
steps = ''.join(f'<section class="step" id="c{i + 1}"><div class="n">0{i + 1}</div><h3>{h}</h3>{img(im, alt, "stepimg", w=1200, h=500)}<p>{p}</p><div class="tip">💡 {t}</div></section>' for i, (h, p, t, im, alt) in enumerate(STEPS))

FAQ = [
    ('What is the best robot vacuum for pet hair?', 'Look for strong suction with automatic carpet boost, rubber or anti-tangle brushes, and AI obstacle avoidance to steer around pet accidents. In our picks, the eufy HydroJet (best overall) and the Roborock Saros 10R (premium) are the strongest fits for homes with pets.'),
    ('LiDAR or camera navigation: which is better?', 'LiDAR maps your home accurately and works in the dark. Camera navigation can also recognize objects but needs light. The best models combine mapping with a camera or 3D sensors for obstacle avoidance.'),
    ('Is a self-emptying robot vacuum worth it?', 'Yes, for most homes. You empty a sealed bag every few weeks instead of a small bin every day, which is cleaner and better for allergies. Check the cost of replacement bags.'),
    ('Do robot vacuums work on thick carpet?', 'Most handle low and medium-pile carpet well. For thick carpet, choose higher suction with carpet boost, and a mop that lifts or a carpet-avoid setting if the robot also mops.'),
    ('How do I choose a robot vacuum that fits under my furniture?', 'Measure the gap under your sofa and bed and compare it with the robot’s height on the product page. Also check the maximum threshold it can climb for door sills and rug edges.'),
]
faq = '<section class="faq" id="faq"><h2>Robot vacuum FAQ</h2>' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ) + '</section>'

guide = f'''<div class="crumb"><a href="/">Home</a> › <a href="/guides/robot-vacuum/">Cleaning</a> › Robot vacuums</div>
<section class="ghead"><div><div class="kick">Smart buying guide · Cleaning</div><h1>Best robot vacuum 2026: how to choose one <i>that actually works</i></h1><p class="lead">Before you buy a robot vacuum, check these 6 things: navigation, suction, obstacle avoidance, height, self-emptying base and mopping. Then pick from our 3 choices for every budget, for pets, carpets and hardwood floors.</p><div class="by"><span>Updated November 2026</span><span>· 7 min read</span><span>· 6 criteria</span></div></div>{img('/assets/img/robot-vacuum.jpg', 'Robot vacuum with LiDAR navigation cleaning a carpet', 'gimg', lazy=False)}</section>
<section class="verdict"><h2 class="kick">Quick answer · Our 3 picks for 2026</h2><div class="picks">{cards}</div><p class="disc">As an Amazon Associate we earn from qualifying purchases, at no extra cost to you. Picks are based on our criteria and on published expert tests, not on paid placements. Product photos on this page are illustrations: see the real photos on Amazon.</p></section>
<div class="two"><div><h2 style="margin-bottom:24px">How to choose a robot vacuum: the 6 things that matter</h2>{steps}{faq}</div>
<aside><div class="check" id="checklist"><h3>Before you buy ✓</h3><ul><li>☐ LiDAR or camera navigation</li><li>☐ Suction that fits your floors</li><li>☐ Obstacle avoidance (if needed)</li><li>☐ Height &amp; threshold checked</li><li>☐ Self-emptying base</li><li>☐ Mop that lifts on carpet</li><li>☐ Price of spare brushes, filters &amp; bags</li></ul><button onclick="window.print()">⬇ Save the checklist</button></div></aside></div>'''

schema = [
    {'@context': 'https://schema.org', '@type': 'Article', 'headline': 'Best robot vacuum 2026: how to choose one that actually works', 'image': [SITE + '/assets/img/robot-vacuum.jpg'], 'datePublished': UPDATED, 'dateModified': UPDATED, 'author': ORG, 'publisher': ORG, 'mainEntityOfPage': SITE + '/guides/robot-vacuum/'},
    {'@context': 'https://schema.org', '@type': 'ItemList', 'name': 'Best robot vacuums 2026', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': p[2].replace('&amp;', '&'), 'url': p[5]} for i, p in enumerate(PICKS)]},
    {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ]},
    {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'}, {'@type': 'ListItem', 'position': 2, 'name': 'Robot vacuums', 'item': SITE + '/guides/robot-vacuum/'}]},
]
write('guides/robot-vacuum/index.html', page('Best Robot Vacuum 2026: How to Choose (6 Things That Matter) + 3 Picks',
                                             'Best robot vacuum 2026 for pets, carpet and hardwood floors: LiDAR vs camera, suction, obstacle avoidance, self-emptying base, plus our 3 picks for every budget and a free checklist.',
                                             '/guides/robot-vacuum/', guide, image='/assets/img/robot-vacuum.jpg', schema=schema, preload_img='/assets/img/robot-vacuum.jpg'))

# ---------- À propos ----------
about = '''<div class="prose"><div class="kick">About</div><h1>How we choose</h1><p>Buy It Smart helps you buy the right product the first time. Every guide starts with the criteria that change your daily life, then gives one pick per budget.</p><h2>Our method</h2><ul><li><b>Criteria first.</b> We explain what to look for before naming any model.</li><li><b>Expert tests &amp; reviews.</b> We cross-check published expert tests and the recurring complaints of verified buyers.</li><li><b>One pick per budget.</b> Small, medium and premium, so everyone finds an option.</li><li><b>Honest limits.</b> We tell you what a product does not do. Specs and prices change: always check the product page.</li></ul><h2>How we earn money</h2><p>As an Amazon Associate we earn from qualifying purchases. When you buy through our links, we may receive a commission at no extra cost to you. It never changes our criteria or our picks.</p><h2>Photos</h2><p>Illustration photos come from Pixabay. Real product photos and prices are on Amazon.</p><h2>Contact</h2><p>Instagram: <a href="https://www.instagram.com/buyitsmartguides/" target="_blank" rel="noopener"><u>@buyitsmartguides</u></a></p></div>'''
write('about/index.html', page('About Buy It Smart & how we choose products', 'How Buy It Smart chooses products: criteria first, expert tests and buyer reviews, one pick per budget.', '/about/', about, schema=[{'@context': 'https://schema.org', **ORG}]))

priv = '''<div class="prose"><div class="kick">Legal</div><h1>Privacy policy</h1><p>Last updated: November 2026.</p><h2>What we collect</h2><p>This site has no account, no form and no newsletter. We do not collect personal data ourselves.</p><h2>Amazon links</h2><p>Buy It Smart is a participant in the Amazon Services LLC Associates Program, an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to Amazon.com. When you click a link to Amazon, Amazon may use cookies to attribute a purchase. Amazon's own privacy notice applies on its website.</p><h2>Hosting</h2><p>The site is hosted by Vercel, which may keep technical logs (such as IP addresses) for security and performance.</p><h2>Contact</h2><p>Questions: Instagram <a href="https://www.instagram.com/buyitsmartguides/" target="_blank" rel="noopener"><u>@buyitsmartguides</u></a>.</p></div>'''
write('privacy/index.html', page('Privacy policy – Buy It Smart', 'Privacy policy of Buy It Smart.', '/privacy/', priv))

pages = [('/', '1.0'), ('/guides/robot-vacuum/', '0.9'), ('/about/', '0.3'), ('/privacy/', '0.1')]
write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">'
      + ''.join(f'<url><loc>{SITE}{p}</loc><lastmod>{UPDATED}</lastmod><priority>{pr}</priority>' + (f'<image:image><image:loc>{SITE}/assets/img/robot-vacuum.jpg</image:loc></image:image>' if 'robot' in p else '') + '</url>' for p, pr in pages) + '</urlset>\n')
print('ok')
