url = "https://qrcode3.p.rapidapi.com/qrcode/text"
photo_uri = "https://www.mirteck.ru/upload/iblock/392/%D0%9C%D0%98%D0%A0%D0%A2%D0%95%D0%9A%20%D0%BB%D0%BE%D0%B3%D0%BE%D0%B7%D0%BD%D0%B0%D0%BA.png"

payload = {
    "data": "https://mirteck.ru/card/?promo=telegram",
    "image": {
        "uri": photo_uri,
        "modules": True
    },
    "style": {
        "module": {
            "color": "#660512",
            "shape": "heavyround"
        },
        "inner_eye": {"shape": "heavyround"},
        "outer_eye": {"shape": "heavyround"},
        "background": {}
    },
    "size": {
        "width": 1000,
        "quiet_zone": 4,
        "error_correction": "M"
    },
    "output": {
        "filename": "qrcode",
        "format": "png"
    }
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "38b38d444dmsh19196db0301b8e1p13d904jsn8fdcbb7fd6fd2025",
    "X-RapidAPI-Host": "qrcode3.p.rapidapi.com"
}
