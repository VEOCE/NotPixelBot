import random

existing_versions = {
    110: [
        '110.0.5481.154',
        '110.0.5481.153',
        '110.0.5481.65',
        '110.0.5481.64',
        '110.0.5481.63',
        '110.0.5481.61'
    ],
    111: [
        "111.0.5563.116",
        '111.0.5563.115',
        '111.0.5563.58',
        '111.0.5563.49'
    ],
    112: [
        '112.0.5615.136',
        '112.0.5615.136',
        '112.0.5615.101',
        '112.0.5615.100',
        '112.0.5615.48'
    ],
    113: [
        '113.0.5672.77',
        '113.0.5672.76'
    ],
    114: [
        '114.0.5735.60',
        '114.0.5735.53'
    ],
    115: [
        '115.0.5790.136'
    ],
    116: [
        '116.0.5845.172',
        '116.0.5845.164',
        '116.0.5845.163',
        '116.0.5845.114',
        '116.0.5845.92'
    ],
    117: [
        '117.0.5938.154',
        '117.0.5938.141',
        '117.0.5938.140',
        '117.0.5938.61',
        '117.0.5938.61',
        '117.0.5938.60'
    ],
    118: [
        '118.0.5993.112',
        '118.0.5993.111',
        '118.0.5993.80',
        '118.0.5993.65',
        '118.0.5993.48'
    ],
    119: [
        '119.0.6045.194',
        '119.0.6045.193',
        '119.0.6045.164',
        '119.0.6045.163',
        '119.0.6045.134',
        '119.0.6045.134',
        '119.0.6045.66',
        '119.0.6045.53'
    ],
    120: [
        '120.0.6099.230',
        '120.0.6099.210',
        '120.0.6099.194',
        '120.0.6099.193',
        '120.0.6099.145',
        '120.0.6099.144',
        '120.0.6099.144',
        '120.0.6099.116',
        '120.0.6099.116',
        '120.0.6099.115',
        '120.0.6099.44',
        '120.0.6099.43'
    ],
    121: [
        '121.0.6167.178',
        '121.0.6167.165',
        '121.0.6167.164',
        '121.0.6167.164',
        '121.0.6167.144',
        '121.0.6167.143',
        '121.0.6167.101'
    ],
    122: [
        '122.0.6261.119',
        '122.0.6261.106',
        '122.0.6261.105',
        '122.0.6261.91',
        '122.0.6261.90',
        '122.0.6261.64',
        '122.0.6261.43'
    ],
    123: [
        '123.0.6312.121',
        '123.0.6312.120',
        '123.0.6312.119',
        '123.0.6312.118',
        '123.0.6312.99',
        '123.0.6312.80',
        '123.0.6312.41',
        '123.0.6312.40'
    ],
    124: [
        '124.0.6367.179',
        '124.0.6367.172',
        '124.0.6367.171',
        '124.0.6367.114',
        '124.0.6367.113',
        '124.0.6367.83',
        '124.0.6367.82',
        '124.0.6367.54'
    ],
    125: [
        '125.0.6422.165',
        '125.0.6422.164',
        '125.0.6422.147',
        '125.0.6422.146',
        '125.0.6422.113',
        '125.0.6422.72',
        '125.0.6422.72',
        '125.0.6422.53',
        '125.0.6422.52'
    ],
    126: [
        '126.0.6478.122',
        '126.0.6478.72',
        '126.0.6478.71',
        '126.0.6478.50'
    ]
}


def generate_random_user_agent(device_type='android', browser_type='chrome'):
    firefox_versions = list(range(100, 127))  # Last 10 versions of Firefox

    if browser_type == 'chrome':
        major_version = random.choice(list(existing_versions.keys()))
        browser_version = random.choice(existing_versions[major_version])
    elif browser_type == 'firefox':
        browser_version = random.choice(firefox_versions)

    if device_type == 'android':
        android_versions = ['8.0', '8.1', '9.0', '10.0', '11.0', '12.0', '13.0', '14.0', '15.0']
        android_device = random.choice([
            'SM-G960F', 'SM-G973F', 'SM-G980F', 'SM-G960U', 'SM-G973U', 'SM-G980U',
            'SM-A505F', 'SM-A515F', 'SM-A525F', 'SM-N975F', 'SM-N986B', 'SM-N981B',
            'SM-F711B', 'SM-F916B', 'SM-G781B', 'SM-G998B', 'SM-G991B', 'SM-G996B',
            'SM-G990E', 'SM-G990B2', 'SM-G990U', 'SM-G990B', 'SM-G990', 'SM-G990',
            'Pixel 2', 'Pixel 2 XL', 'Pixel 3', 'Pixel 3 XL', 'Pixel 4', 'Pixel 4 XL',
            'Pixel 4a', 'Pixel 5', 'Pixel 5a', 'Pixel 6', 'Pixel 6 Pro', 'Pixel 6 XL',
            'Pixel 6a', 'Pixel 7', 'Pixel 7 Pro', 'Pixel 7a', 'Pixel 8', 'Pixel 8 Pro',
            'IN2010', 'IN2023', 'LE2117', 'LE2123', 'OnePlus Nord', 'IV2201', 'NE2215',
            'CPH2423', 'NE2210', 'Mi 9', 'Mi 10', 'Mi 11', 'Mi 12', 'Mi 13', 'Mi 14',
            'Redmi Note 8', 'Redmi Note 8 Pro', 'Redmi Note 9', 'Redmi Note 9 Pro',
            'Redmi Note 10', 'Redmi Note 10 Pro', 'Redmi Note 11', 'Redmi Note 11 Pro',
            'Redmi Note 12', 'Redmi Note 12 Pro', 'Redmi Note 13', 'Redmi Note 13 Pro',
            'VOG-AL00', 'ANA-AL00', 'TAS-AL00', 'OCE-AN10', 'J9150', 'J9210',
            'LM-G820', 'L-51A', 'Nokia 8.3', 'Nokia 9 PureView', 'POCO F5', 'POCO F5 Pro',
            'POCO M3', 'POCO M3 Pro', 'POCO X3', 'POCO X3 Pro', 'POCO X4', 'POCO X4 Pro',
            'POCO X5', 'POCO X5 Pro', 'POCO F6', 'POCO F6 Pro', 'Xperia 1 V', 'Xperia 5 V',
            'Xperia 10 V', 'ROG Phone 7', 'ROG Phone 7 Ultimate', 'Zenfone 10',
            'Galaxy S24', 'Galaxy S24+', 'Galaxy S24 Ultra', 'Galaxy A54', 'Galaxy A34',
            'Galaxy M54', 'Galaxy M34', 'Nothing Phone 2', 'Nothing Phone 2a'
        ])
        android_version = random.choice(android_versions)
        if browser_type == 'chrome':
            return (f"Mozilla/5.0 (Linux; Android {android_version}; {android_device}) AppleWebKit/537.36 "
                    f"(KHTML, like Gecko) Chrome/{browser_version} Mobile Safari/537.36")
        elif browser_type == 'firefox':
            return (f"Mozilla/5.0 (Android {android_version}; Mobile; rv:{browser_version}.0) "
                    f"Gecko/{browser_version}.0 Firefox/{browser_version}.0")

    elif device_type == 'ios':
        ios_versions = ['12.0', '13.0', '14.0', '15.0', '16.0', '17.0', '17.1', '17.2', '17.3', '17.4', '18.0']
        ios_devices = [
            'iPhone 11', 'iPhone 11 Pro', 'iPhone 11 Pro Max',
            'iPhone 12', 'iPhone 12 Mini', 'iPhone 12 Pro', 'iPhone 12 Pro Max',
            'iPhone 13', 'iPhone 13 Mini', 'iPhone 13 Pro', 'iPhone 13 Pro Max',
            'iPhone 14', 'iPhone 14 Plus', 'iPhone 14 Pro', 'iPhone 14 Pro Max',
            'iPhone 15', 'iPhone 15 Plus', 'iPhone 15 Pro', 'iPhone 15 Pro Max',
            'iPad Pro 11-inch', 'iPad Pro 12.9-inch', 'iPad Air', 'iPad mini'
        ]
        ios_version = random.choice(ios_versions)
        ios_device = random.choice(ios_devices)
        if browser_type == 'chrome':
            return (f"Mozilla/5.0 ({ios_device}; CPU iPhone OS {ios_version.replace('.', '_')} like Mac OS X) "
                    f"AppleWebKit/537.36 (KHTML, like Gecko) CriOS/{browser_version} Mobile/15E148 Safari/604.1")
        elif browser_type == 'firefox':
            return (f"Mozilla/5.0 ({ios_device}; CPU iPhone OS {ios_version.replace('.', '_')} like Mac OS X) "
                    f"AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/{browser_version}.0 Mobile/15E148 Safari/605.1.15")

    elif device_type == 'windows':
        windows_versions = ['10.0', '11.0']
        windows_builds = ['19041', '19042', '19043', '19044', '19045', '22000', '22621', '22631']
        windows_version = random.choice(windows_versions)
        windows_build = random.choice(windows_builds)
        if browser_type == 'chrome':
            return (f"Mozilla/5.0 (Windows NT {windows_version}; Win64; x64; rv:{windows_build}.0) AppleWebKit/537.36 (KHTML, like Gecko) "
                    f"Chrome/{browser_version} Safari/537.36")
        elif browser_type == 'firefox':
            return (f"Mozilla/5.0 (Windows NT {windows_version}; Win64; x64; rv:{browser_version}.0) "
                    f"Gecko/{browser_version}.0 Firefox/{browser_version}.0")

    elif device_type == 'ubuntu':
        ubuntu_versions = ['18.04', '20.04', '22.04', '23.04', '23.10', '24.04']
        ubuntu_version = random.choice(ubuntu_versions)
        if browser_type == 'chrome':
            return (f"Mozilla/5.0 (X11; Linux x86_64; Ubuntu {ubuntu_version}) AppleWebKit/537.36 (KHTML, like Gecko) "
                    f"Chrome/{browser_version} Safari/537.36")
        elif browser_type == 'firefox':
            return (f"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{browser_version}.0) Gecko/{browser_version}.0 "
                    f"Firefox/{browser_version}.0")

    return None
