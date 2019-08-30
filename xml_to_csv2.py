import csv
import xml.etree.ElementTree as ET

tree = ET.parse('news_feed2.xml')
root = tree.getroot()
print(root)

xml_csv = open('news2.csv', 'w')
item_csv = open('item2.csv', 'w')


list_head = []
csv_writer = csv.writer(xml_csv)
item_writer = csv.writer(item_csv)

ns = {'atom': 'http://www.w3.org/2005/Atom',
      'dc': 'http://purl.org/dc/elements/1.1/',
      'media': 'http://search.yahoo.com/mrss/'}
y = root.find('channel').findall('atom:link', ns)[0].get('href')
print(y)

count = 0
for i in root.findall('channel'):
    # print(i)
    list_nodes = []
    if count == 0:
        title = i.find('title').tag
        list_head.append(title)

        link = i.find('link').tag
        list_head.append(link)

        # atom = i.find('atom:i', ns)
        list_head.append('atom')

        description = i.find('description').tag
        list_head.append(description)

        language = i.find('language').tag
        list_head.append(language)

        copyright = i.find('copyright').tag
        list_head.append(copyright)

        lastBuildDate = i.find('lastBuildDate').tag
        list_head.append(lastBuildDate)

        image = i.findall('image')
        for img in image:
            img_title = img.find('title').tag
            list_head.append('img_'+img_title)
            img_url = img.find('url').tag
            list_head.append('img_'+img_url)
            img_link = img.find('link').tag
            list_head.append("img_"+img_link)

        item = i.find('item').tag
        list_head.append(item)

        csv_writer.writerow(list_head)
        count += 1

    title = i.find('title').text
    list_nodes.append(title)

    link = i.find('link').text
    list_nodes.append(link)

    atom = i.findall('atom:link', ns)[0].get('href')
    list_nodes.append(atom)

    description = i.find('description').text
    list_nodes.append(description)

    language = i.find('language').text
    list_nodes.append(language)

    copyright = i.find('copyright').text
    list_nodes.append(copyright)

    lastBuildDate = i.find('lastBuildDate').text
    list_nodes.append(lastBuildDate)

    image = i.findall('image')
    for img in image:
        img_title = img.find('title').text
        list_nodes.append(img_title)
        img_url = img.find('url').text
        list_nodes.append(img_url)
        img_link = img.find('link').text
        list_nodes.append(img_link)


    csv_writer.writerow(list_nodes)

xml_csv.close()

item_head = []
k = 0
for j in root.findall('channel'):
    # print('dfgdf')
    for i in j.findall('item'):
        # print('x')
        item_node = []
        item_category = []
        if k == 0:
            # print('xyz')
            title = i.find('title').tag
            item_head.append(title)

            link = i.find('link').tag
            item_head.append(link)

            # atom = i.find('atom').tag
            item_head.append('atom')

            description = i.find('description').tag
            item_head.append(description)


            # creator = i.find('dc:creator').tag
            item_head.append('creator')

            pubDate = i.find('pubDate').tag
            item_head.append(pubDate)

            category = i.find('category').tag
            item_head.append(category)

            # media_content = i.find('media:content').tag
            item_head.append('media_content')

            # media_credit = i.find('media:credit').tag
            item_head.append('media_credit')

            # media_description = i.find('media:description').tag
            item_head.append('media_description')

            item_writer.writerow(item_head)
            k += 1

        title = i.find('title').text
        item_node.append(title)

        link = i.find('link').text
        item_node.append(link)

        atom = i.find('atom:link', ns).get('href')
        item_node.append(atom)

        description = i.find('description').text
        item_node.append(description)

        # creator = i.find('dc:creator', ns).text
        # item_node.append(creator)

        pubDate = i.find('pubDate').text
        item_node.append(pubDate)

        category = i.findall('category')
        item_category = [z.text for z in category]
        item_node.append(item_category)
        try:
            media_content = i.find('media:content', ns).get('url')
        except Exception as e:
            continue
        else:
            item_node.append(media_content)
            #
        try:
            media_credit = i.find('media:credit', ns).text
        except Exception as e:
            continue
        else:
            item_node.append(media_credit)
            #
        try:
            media_description = i.find('media:description', ns).text
        except Exception as e:
            continue
        else:
            item_node.append(media_description)

        item_writer.writerow(item_node)

item_csv.close()
