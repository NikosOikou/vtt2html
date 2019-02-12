import os
import glob


TPL_START = """
<html>
   <head>
      <meta http-equiv="content-type" content="text/html; charset=UTF-8">
      <link rel="stylesheet" href=lrstyle.css type="text/css">
   </head>
   <body>
      <hr class="lrhr">
      <table class="lrtext">
         <th class="lr2th"></th>
         <th class="lr2th"></th>
"""

TPL_END = """
      </table>
   </body>
</html>
"""

TPL_FILL_1 = """
<tr>
   <td>{text_fi}</td>
   <td>{text_en}</td>
</tr>
"""

TPL_FILL_2 = """
<tr class=lraltline>
   <td>{text_fi}</td>
   <td>{text_en}</td>
</tr>
"""

TPL_FILL_3 = """
<tr class=video_number>
   <td>{text_fi}</td>
   <td>{text_en}</td>
</tr>
"""

total = [TPL_START]

for j, f in enumerate(glob.glob('input/*.vtt'), start=1):
    data = open(f).readlines()
    sentences_fi = data[5::4]
    sentences_en = data[6::4]
    parts = [TPL_START]

    filename = os.path.basename(f)
    title = filename.split('! ')[1].split('-')[0]
    total.append(TPL_FILL_3.format(text_fi=str(j) + '. ' + title, text_en=''))

    for i, (x, y) in enumerate(zip(sentences_fi, sentences_en)):
        tpl = TPL_FILL_1 if i % 2 else TPL_FILL_2
        fill = tpl.format(text_fi=x, text_en=y)
        parts.append(fill)
        total.append(fill)
    parts.append(TPL_END)
    result = '\n'.join(parts)

    output_file = 'output/' + filename + '.html'
    with open(output_file, 'w') as fw:
        fw.write(result)

total.append(TPL_END)
result = '\n'.join(total)

with open('output/bigfile.html', 'w') as fw:
    fw.write(result)


