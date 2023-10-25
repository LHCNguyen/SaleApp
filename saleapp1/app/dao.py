def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    },{
        'id': 2,
        'name': 'Tablet'
    }]
def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'iPhone 16',
        'price': 20000000,
        'image': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fvtv.vn%2Fcong-nghe%2Fiphone-16-se-co-chip-a18-va-a18-pro-20231024143238614.htm&psig=AOvVaw20OkVQQbyrz0bn3RJc6_6T&ust=1698304563725000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCNjP99fTkIIDFQAAAAAdAAAAABAD'
    }, {
        'id': 2,
        'name': 'Galaxy s22 ultra ',
        'price': 99999999,
        'image': 'https://www.google.com/aclk?sa=l&ai=DChcSEwiajOmO1JCCAxWxwBYFHXhvCMMYABABGgJ0bA&ase=2&gclid=EAIaIQobChMImozpjtSQggMVscAWBR14bwjDEAQYASABEgLOF_D_BwE&sig=AOD64_3Ege4QRw4Hoy0IjY_eb0KSEsnt3g&ctype=5&nis=5&adurl&ved=2ahUKEwi2p96O1JCCAxVOilYBHV5tAysQvhd6BAgBEHM'
    }]
    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products