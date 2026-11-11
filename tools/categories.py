# Guides de catégorie Café et Chambre (même gabarit que les guides robot / friteuse).
# Les caractéristiques citées viennent des pages fabricant ou de leurs fiches revendeur
# (vérifiées le 2026-11-11). Exécuté depuis build.py (exec), qui fournit page(), img(), check_js, SITE, TAG, ORG, UPDATED.

CAT_DATE = '2026-11-11'

def _amz_s(q):
    return f'https://www.amazon.com/s?k={q}&tag={TAG}'

CATS = [
 dict(key='coffee', url='/guides/coffee-maker/', crumb='Coffee', label='Coffee makers', noun='coffee maker', h2noun='a coffee maker',
      hero='/assets/img/cf-breakfast-coffee.jpg', hero_alt='Morning coffee on a breakfast table next to a coffee maker',
      title_tag='Best Coffee Maker 2026: How to Choose (Drip, Pod or Espresso) + 3 Picks',
      desc='Best coffee maker 2026: drip vs pod vs espresso vs French press, grinder, brew temperature, cost per cup and cleaning, plus our 3 picks for every budget and a free checklist.',
      h1='Best coffee maker 2026: how to choose <i>the right one for your mornings</i>',
      headline='Best coffee maker 2026: how to choose the right one for your mornings',
      lead='Before you buy a coffee maker, check these 6 things: your brew style, the grinder, brew temperature, the real cost per cup, milk drinks, and cleaning. Then pick from our 3 choices for every budget.',
      read='6 min read', card_t='Best coffee maker 2026: drip, pod or espresso?', card_d='Brew style, grinder, cost per cup… and 3 picks for every budget.',
      picks=[
       ('BEST BUDGET', 'b1', 'Keurig K-Mini Single-Serve Coffee Maker', 'One person, small kitchens, coffee in one minute of effort',
        ['Brews one cup from 6 to 12 oz with K-Cup pods', 'Less than 5 inches wide: fits almost any counter', 'No carafe, no filter, nothing to measure', 'Pods cost more per cup than ground coffee: count it'],
        'https://link.amazon/B0hgdV6Ne', '/assets/img/cf-pod-coffee-maker.jpg', 'Compact single-serve pod coffee maker (illustration)', ''),
       ('BEST OVERALL', 'b2', 'OXO Brew 8-Cup Coffee Maker', 'Couples and families who drink real drip coffee every day',
        ['SCA Certified Home Brewer: tested to brew at the right temperature and time', 'Thermal stainless-steel carafe keeps coffee hot without a hot plate', '40 oz water tank, up to 8 cups', 'Can also brew a single cup into your mug'],
        f'https://www.amazon.com/dp/B07H9G93WK?tag={TAG}', '/assets/img/cf-drip-coffee-maker.jpg', 'Drip coffee maker with a thermal carafe (illustration)', ' top'),
       ('PREMIUM', 'b3', 'Breville Bambino Plus Espresso Machine', 'Latte and cappuccino lovers who want café drinks at home',
        ['ThermoJet heating: ready to brew in about 3 seconds (brand claim)', 'Automatic steam wand: 3 milk temperatures and 3 textures', '54 mm portafilter with single and dual-wall filters', 'Best with freshly ground beans: budget for a burr grinder'],
        'https://link.amazon/B005mn5Mz', '/assets/img/cf-espresso-machine.jpg', 'Compact espresso machine with a steam wand (illustration)', ''),
      ],
      steps=[
       ('Start with how you drink coffee', 'A big pot for the family? Drip. One quick cup before work? A pod machine. Lattes and cappuccinos? Espresso with a steam wand. A slow weekend ritual on a small budget? French press or pour-over. Choosing the brew style first saves you from paying for features you will never use.', 'Count how many cups your home drinks on a weekday: 1 to 2 points to single-serve, 4 or more points to a drip machine with a carafe.', '/assets/img/cf-french-press-pour-over.jpg', 'French press and pour-over coffee brewing on a counter'),
       ('The grinder matters as much as the machine', 'Coffee loses its aroma quickly once ground. A burr grinder crushes beans to an even size, so the water extracts them evenly; a blade grinder chops them into dust and chunks, which tastes both bitter and sour. For espresso, a fine and consistent grind is essential.', 'If your budget is tight, a decent burr grinder with a simple brewer often tastes better than an expensive machine with pre-ground coffee.', '/assets/img/cf-burr-grinder.jpg', 'Burr coffee grinder with whole coffee beans'),
       ('Brew temperature: the hidden spec', 'Many cheap drip machines never get the water hot enough, which gives weak, flat coffee. The Specialty Coffee Association (SCA) certifies home brewers that hit its brewing standards, including a water temperature of about 197.6 to 204.8°F (92 to 96°C) and a set brew time.', 'Look for the “SCA Certified Home Brewer” mark when you buy a drip coffee maker: it is an independent lab test, not a marketing badge.', '/assets/img/cf-drip-coffee-maker.jpg', 'Drip coffee maker brewing into a carafe'),
       ('Count the real cost per cup', 'Pod machines are cheap to buy but cost more per cup than ground coffee, every day, for years. Also count filters, descaling solution and, for espresso, a grinder and a milk jug. Over a year, the running costs often matter more than the price of the machine.', 'Divide the price of a box of pods by the number of pods, then do the same for a bag of beans (about 0.35 oz of coffee per cup): the difference is your yearly cost.', '/assets/img/cf-pod-coffee-maker.jpg', 'Single-serve pod coffee maker with coffee pods'),
       ('Milk drinks? Check the steam wand', 'If you love lattes, the steam wand decides how good they are. Automatic wands texture the milk for you; manual wands give more control but need practice. A separate milk frother is a cheaper option with a drip or pod machine.', 'Only buy an espresso machine if you will use it most days: it needs a few minutes of cleaning after each session.', '/assets/img/cf-espresso-machine.jpg', 'Espresso machine steaming milk for a latte'),
       ('Cleaning and descaling', 'Coffee oils and limescale change the taste over time and can slow the machine down. Check that the carafe, filter basket and drip tray come out easily, and that the brand explains how to descale. Hard tap water means descaling more often.', 'A thermal carafe keeps coffee hot without a hot plate, which also avoids that burnt taste after 20 minutes.', None, None),
      ],
      faq=[
       ('What is the best type of coffee maker for home?', 'It depends on how you drink coffee. A drip coffee maker is best for several cups at once, a pod machine for one fast cup, an espresso machine for lattes and cappuccinos, and a French press or pour-over for a low-cost, hands-on ritual.'),
       ('Is a single-serve pod coffee maker worth it?', 'It is worth it for speed and convenience if you drink one or two cups a day. Pods cost more per cup than ground coffee, so compare the yearly cost before you buy.'),
       ('What does SCA certified mean for a coffee maker?', 'The Specialty Coffee Association tests home brewers in its lab and certifies the ones that meet its standards for water temperature, brew time and extraction. It is one of the few independent quality marks for drip coffee makers.'),
       ('Do I need a grinder for an espresso machine?', 'For the best espresso, yes: espresso needs a fine, even grind made just before brewing. Some machines include dual-wall filters that work with pre-ground coffee, which is easier but gives less control over taste.'),
       ('How often should I descale my coffee maker?', 'Follow the brand’s instructions. As a rule, descale more often if your tap water is hard, and as soon as the machine brews more slowly or the coffee tastes flat.'),
      ],
      check=[('Brew style chosen (drip, pod, espresso, French press)', 1), ('Cups per day counted', 1), ('Grinder planned (burr, not blade)', 2), ('SCA mark or brew temperature checked', 3), ('Cost per cup compared (pods vs beans)', 4), ('Milk drinks: steam wand or frother', 5), ('Removable parts + descaling plan', 6)],
      check_key='bis-check-coffee'),
 dict(key='sheets', url='/guides/bed-sheets/', crumb='Bedroom', label='Bed sheets', noun='bed sheets', h2noun='bed sheets',
      hero='/assets/img/bd-white-cotton-sheets.jpg', hero_alt='White cotton sheets on a neatly made bed',
      title_tag='Best Bed Sheets 2026: Percale vs Sateen, Cotton vs Linen + 3 Picks',
      desc='Best bed sheets 2026: percale vs sateen, cotton, linen or microfiber, the thread count myth, deep pockets and OEKO-TEX, plus our 3 picks for every budget and a free checklist.',
      h1='Best bed sheets 2026: how to choose sheets <i>you will love sleeping in</i>',
      headline='Best bed sheets 2026: how to choose sheets you will love sleeping in',
      lead='Before you buy bed sheets, check these 6 things: your mattress depth, the weave, the fiber, what thread count really means, the labels worth trusting, and how you sleep. Then pick from our 3 choices for every budget.',
      read='6 min read', card_t='Best bed sheets 2026: percale, sateen or linen?', card_d='Weave, fiber, thread count, deep pockets… and 3 picks for every budget.',
      picks=[
       ('BEST BUDGET', 'b1', 'Mellanni Brushed Microfiber Sheet Set', 'Guest rooms, kids’ beds and tight budgets',
        ['Double-brushed microfiber (polyester): soft and wrinkle-resistant', 'Deep pockets for mattresses up to about 16 inches (check your size)', 'All-around elastic on the fitted sheet', 'Can sleep warmer than cotton or linen'],
        'https://link.amazon/B00KTzdij', '/assets/img/bd-sheet-set.jpg', 'Folded bed sheet set with pillowcases (illustration)', ''),
       ('BEST OVERALL', 'b2', 'California Design Den 400 Thread Count Cotton Sateen Sheets', 'Most sleepers who want soft, smooth cotton',
        ['100% long-staple cotton, sateen weave: smooth with a soft sheen', 'OEKO-TEX Standard 100 certified (per the brand)', 'Deep pockets up to 16 inches on most sizes (15 inches on Twin and Twin XL)', 'Sateen feels warmer than percale: hot sleepers, read step 2'],
        'https://link.amazon/B04zJbXzw', '/assets/img/bd-white-cotton-sheets.jpg', 'Smooth white cotton sateen sheets on a bed (illustration)', ' top'),
       ('PREMIUM', 'b3', 'Simple&amp;Opulence 100% Linen Sheet Set', 'Hot sleepers and lovers of the relaxed, natural look',
        ['100% stone-washed French flax linen', 'OEKO-TEX Standard 100 certified (per the brand)', 'Fitted sheet with a 14-inch deep pocket: measure your mattress first', 'Linen wrinkles by nature: that relaxed look is part of it'],
        'https://link.amazon/B04NsUeHM', '/assets/img/bd-linen-sheets.jpg', 'Natural linen sheets with a relaxed texture (illustration)', ''),
      ],
      steps=[
       ('Measure your mattress depth first', 'The most common sheet problem is a fitted sheet that pops off the corners. Measure your mattress from the bottom seam to the top, including any topper, then choose a pocket depth at least 1 to 2 inches deeper. Standard pockets fit thinner mattresses; “deep pocket” sets fit thicker ones.', 'Write your mattress depth on your phone: you will need it every time you buy sheets or a mattress protector.', '/assets/img/bd-measure-mattress-depth.jpg', 'Measuring the depth of a mattress with a tape measure'),
       ('Percale or sateen: the weave decides the feel', 'Percale is a simple one-over, one-under weave: crisp, matte and cool, like a hotel shirt. Sateen floats more threads on the surface: smoother, with a soft sheen and a heavier drape, but it feels warmer and can pill more easily over time.', 'Hot sleeper? Start with percale or linen. Always cold? Sateen or brushed microfiber will feel cozier.', '/assets/img/bd-percale-vs-sateen.jpg', 'Close-up of percale and sateen cotton fabric textures'),
       ('Cotton, linen or microfiber?', 'Cotton is the all-rounder: breathable, durable and easy to wash, and long-staple cotton feels softer and lasts longer. Linen (made from flax) is very breathable, gets softer with every wash and wrinkles by nature. Microfiber (polyester) is soft, cheap and wrinkle-resistant, but breathes less.', 'Check the label for “100%” cotton or linen: blends are fine, but they should be priced lower.', '/assets/img/bd-linen-sheets.jpg', 'Natural linen bed sheets on an unmade bed'),
       ('The thread count myth', 'Thread count is the number of threads in a square inch of fabric. More is not always better: beyond a few hundred, very high numbers often come from thin multi-ply threads counted several times. Fiber quality and weave matter more than a big number on the box.', 'For cotton, a mid-range thread count in good long-staple cotton usually beats a very high count in short-staple cotton. Linen is measured differently and rarely shows a thread count.', '/assets/img/bd-white-cotton-sheets.jpg', 'Close-up of soft white cotton sheets'),
       ('Labels worth trusting', 'OEKO-TEX Standard 100 means the finished fabric was tested for a list of harmful substances: it is a safety label, not a quality or organic label. GOTS certifies organic fibers and the way they are processed. Check the certificate number on the official website if a brand shows one.', '“Organic” on its own is a marketing word: look for a certification and a certificate number.', '/assets/img/bd-sheet-set.jpg', 'Folded sheet set with a care label'),
       ('Sleep hot? Wash smart', 'If you wake up warm, choose breathable fibers (linen, cotton percale) and avoid heavy sateen or microfiber. Wash new sheets before the first night, use warm rather than very hot water, and avoid over-drying: it keeps the fibers soft and limits shrinking.', 'Two sets per bed is the easy rule: one on the bed, one in the wash, and both last longer.', '/assets/img/bd-bedroom-night.jpg', 'Calm bedroom at night with a made bed'),
      ],
      faq=[
       ('What are the best sheets for hot sleepers?', 'Breathable fibers and a cool weave: linen or cotton percale. Sateen and microfiber feel smoother or softer but usually sleep warmer.'),
       ('Percale or sateen: which is better?', 'Neither is better, they feel different. Percale is crisp, matte and cool; sateen is smooth, slightly shiny and warmer. Choose by how you sleep and the feel you like.'),
       ('What thread count is best for sheets?', 'There is no magic number. Fiber quality and weave matter more: good long-staple cotton at a mid-range thread count usually feels and lasts better than a very high count made with thin multi-ply threads.'),
       ('How do I know if I need deep pocket sheets?', 'Measure your mattress depth, including any topper. Choose a fitted sheet with a pocket at least 1 to 2 inches deeper than that number.'),
       ('What does OEKO-TEX certified mean for sheets?', 'OEKO-TEX Standard 100 means the fabric was tested for a list of harmful substances. It is a product safety label, not a sign of organic fibers or of quality.'),
      ],
      check=[('Mattress depth measured (+ topper)', 1), ('Weave chosen: percale (cool) or sateen (smooth)', 2), ('Fiber chosen: cotton, linen or microfiber', 3), ('Not fooled by a huge thread count', 4), ('Certificate checked (OEKO-TEX / GOTS)', 5), ('Hot or cold sleeper: matched to the fiber', 6), ('Care label read (wash + dry)', 6)],
      check_key='bis-check-sheets'),
]


def _cat_guide(c):
    cards = ''.join(f'''<article class="pick{top}"><span class="badge {bc}">{b}</span><div class="phead"><a class="pimg" href="{u}" target="_blank" rel="sponsored nofollow noopener">{img(im, alt, w=800, h=600)}</a><h3 class="h4">{n}</h3></div><div class="for">Best for: {f}</div><ul>{''.join(f'<li>{x}</li>' for x in pts)}</ul><a class="amz" href="{u}" target="_blank" rel="sponsored nofollow noopener">See photos &amp; price on Amazon →</a><div class="price">Price and availability change often: check on Amazon</div></article>''' for b, bc, n, f, pts, u, im, alt, top in c['picks'])
    steps = ''.join(f'<section class="step" id="c{i + 1}"><div class="shead">{img(im, alt, "stepimg", w=800, h=450) if im else ""}<div><div class="n">0{i + 1}</div><h3>{h}</h3></div></div><p>{p}</p><div class="tip">💡 {t}</div></section>' for i, (h, p, t, im, alt) in enumerate(c['steps']))
    faq = f'<section class="faq" id="faq"><h2>{c["label"]} FAQ</h2>' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in c['faq']) + '</section>'
    chk = ''.join(f'<li><label><input type="checkbox" data-i="{i}"><span>{t}</span></label><a href="#c{n}" class="why" aria-label="Why: {t}">why?</a></li>' for i, (t, n) in enumerate(c['check']))
    body = f'''<div class="crumb"><a href="/">Home</a> › <a href="{c["url"]}">{c["crumb"]}</a> › {c["label"]}</div>
<section class="ghead"><div><div class="kick">Smart buying guide · {c["crumb"]}</div><h1>{c["h1"]}</h1><p class="lead">{c["lead"]}</p><div class="by"><span>Updated November 2026</span><span>· {c["read"]}</span><span>· 6 criteria</span></div></div>{img(c["hero"], c["hero_alt"], 'gimg', lazy=False)}</section>
<section class="verdict" id="picks"><h2 class="kick">Quick answer · Our 3 picks for 2026</h2><div class="picks">{cards}</div><p class="disc">As an Amazon Associate we earn from qualifying purchases, at no extra cost to you. Picks are based on our criteria and on brand specs, not on paid placements. Product photos on this page are illustrations: see the real photos, sizes and current specs on Amazon.</p></section>
<div class="two"><div><h2 style="margin-bottom:24px">How to choose {c["h2noun"]}: the 6 things that matter</h2>{steps}{faq}</div>
<aside><div class="check" id="checklist"><h3>Before you buy ✓</h3><p class="cprog"><span id="cnum">0</span>/{len(c["check"])} checked</p><div class="cbar"><i id="cbar"></i></div><ul id="clist">{chk}</ul><p class="cdone" id="cdone" hidden>✓ You’re ready! <a href="#picks">See our 3 picks →</a></p><button type="button" id="csave">⬇ Save the checklist (PDF)</button><button type="button" class="creset" id="creset">Reset</button></div></aside></div>{check_js(c["check_key"])}'''
    schema = [
        {'@context': 'https://schema.org', '@type': 'Article', 'headline': c['headline'], 'image': [SITE + c['hero']], 'datePublished': CAT_DATE, 'dateModified': CAT_DATE, 'author': ORG, 'publisher': ORG, 'mainEntityOfPage': SITE + c['url']},
        {'@context': 'https://schema.org', '@type': 'ItemList', 'name': c['headline'].split(':')[0], 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': p[2].replace('&amp;', '&'), 'url': p[5]} for i, p in enumerate(c['picks'])]},
        {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in c['faq']]},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'}, {'@type': 'ListItem', 'position': 2, 'name': c['label'], 'item': SITE + c['url']}]},
    ]
    write(c['url'].strip('/') + '/index.html', page(c['title_tag'], c['desc'], c['url'], body, image=c['hero'], schema=schema, preload_img=c['hero']))


for _c in CATS:
    _cat_guide(_c)
