from lxml import etree

root = etree.fromstring('''
<svg width="35" height="35" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M20.5 14.3751H17.875V19.1876C17.875 20.3951 16.8949 21.3751 15.6874 21.3751C14.48 21.375 13.5 20.395 13.5 19.1875C13.5 17.98 14.48 17 15.6875 17C16.1819 17 16.6325 17.1707 17 17.4463V12.625H20.5V14.3751Z" fill="url(#paint0_linear)"/>
<path d="M19.5488 19.0918V22.1646L21.9332 20.6282L19.5488 19.0918Z" fill="#AFC476"/>
<path d="M23.0612 24H10.9383C10.4211 24 10 23.5789 10 23.0617V10.9388C10 10.4211 10.4211 10 10.9383 10H23.0612C23.5789 10 24 10.4211 24 10.9388V23.0617C24 23.5789 23.5789 24 23.0612 24ZM10.9383 10.9333L10.9333 23.0616L23.0612 23.0666C23.0648 23.0666 23.0667 23.0639 23.0667 23.0616V10.9388L10.9383 10.9333Z" fill="#AFC476"/>
<defs>
<linearGradient id="paint0_linear" x1="13.5" y1="17" x2="20.5" y2="17" gradientUnits="userSpaceOnUse">
<stop stop-color="#08A5FF"/>
<stop offset="0.2544" stop-color="#41FFFC"/>
<stop offset="0.5193" stop-color="#8AFF18"/>
<stop offset="0.7614" stop-color="#FFFE51"/>
<stop offset="1" stop-color="#FFA856"/>
</linearGradient>
</defs>
</svg>
''')

width = None
height = None

for child in root.iter():
    if width is None:
        _width = child.get('width')
        if _width is None:
            _width = child.get('viewBox')
            if _width is not None:
                _width = _width.split(' ')[-2]
        if _width is not None:
            width = float(_width)
    if height is None:
        _height = child.get('height')
        if _height is None:
            _height = child.get('viewBox')
            if _height is not None:
                _height = _height.split(' ')[-1]
        if _height is not None:
            height = float(_height)
    _gradient_units = child.get('gradientUnits')
    if _gradient_units is not None and _gradient_units == 'objectBoundingBox':
        child.set('gradientUnits', 'userSpaceOnUse')
        if width is not None:
            xs = ['x1', 'x2']
            for x in xs:
                if child.get(x) is not None:
                    child.set(x, '{:.2f}'.format(float(child.get(x)) * width))
        if height is not None:
            ys = ['y1', 'y2']
            for y in ys:
                if child.get(y) is not None:
                    child.set(y, '{:.2f}'.format(float(child.get(y)) * height))
print(etree.tostring(root, encoding="unicode", pretty_print=True))