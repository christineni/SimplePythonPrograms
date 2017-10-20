import webbrowser
import xml.etree.ElementTree as ET

__author__ = 'cni12345'


def main():
    parse_input()
    open_browser()


def parse_input():
    global name, desc, direction, link, phone, lat, long, email
    try:
        file = open('RIDB_USGovt_RecreationSites.xml', 'r', encoding="utf8")
        tree = ET.parse(file)
        write_to_html()

        # Iterate through all elements of tree
        for item in tree.iterfind('RecArea'):
            # Loop through all the elements to obtain data about each RecArea
            for child in item:
                name = item.findtext('RecAreaName')
                desc = item.findtext('RecAreaDescription')
                if item.findtext('RecAreaLatitude'):
                    lat = item.findtext('RecAreaLatitude')
                    long = item.findtext('RecAreaLongitude')
                    link = 'http://www.google.com/maps/@'+lat+','+long+',10z'
                else:
                    lat = ''
                    long = ''
                    link = ''

                if item.findtext('RecAreaPhone'):
                    phone = item.findtext('RecAreaPhone')
                else:
                    phone = ''

                if item.findtext('RecAreaEmail'):
                    email = item.findtext('RecAreaEmail')
                else:
                    email = ''
                if item.findtext('RecAreaDirections'):
                    direction = item.findtext('RecAreaDirections')
                else:
                    direction = ''

            write_info()

    except ET.ParseError as err:
        print('Error: Unable to parse file', err)

    except Exception as err:
        print('Error:', err)


# Function to write heading and title to html file
def write_to_html():
    file = 'NC_RecreationAreas.html'
    html_out = open(file, 'a')
    html_out.write('<!DOCTYPE html>\n')
    html_out.write('<html>\n')
    html_out.write('<head>\n')
    html_out.write('<title>North Carolina Recreational Areas</title>\n')
    html_out.write('<link href="style.css" rel="stylesheet" />\n')
    html_out.write('</head>\n')
    html_out.write('<body>\n')
    html_out.write('<h1>North Carolina Recreational Areas</h1>\n')


# Function to write parsed data to body of html file
def write_info():
    file = 'NC_RecreationAreas.html'
    html_out = open(file, 'a')
    html_out.write('<body>\n')
    html_out.write("<h2><a href ='"+link+"'>"+name+'</a></h2>\n')
    html_out.write('<p>'+desc+'</p>\n')
    html_out.write('<h3>'+'Directions'+'</h3>\n')
    html_out.write('<p>'+direction+'</p>\n')
    html_out.write('<h4>Contact: '+phone+', '+email+'</h4>\n')
    html_out.write('</body>')
    html_out.write('</html>')
    html_out.close()


# Function to open html file in a new browser tab
def open_browser():
    file = 'NC_RecreationAreas.html'
    html_out = open(file, 'a')
    webbrowser.open_new_tab(html_out.name)

# Call on main()
main()
