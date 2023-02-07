#!/usr/bin/env python3
import math

W = ":alphabet-white-"
Y = ":alphabet-yellow-"


fonts = {
    'none': "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ",
    'border': "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡 ",
    'bold': "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗 ",
    'bold-sans': "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵 ",
    'bold-italic': "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗 ",
    'ceasar': "AMWOEZKFYBVXPQCGDLJRITNUHSbfnzuymvokwaecxjghrtqpisld321465897 ",
    'circle': "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ0123456789 ",
    'circle-bold': "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩0123456789 ",
    'double': "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡 ",
    'fraktur': "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷0123456789 ",
    'fraktur-bold': "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗 ",
    'italic': "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻0123456789 ",
    'italic-sans': "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻0123456789 ",
    'mono': "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿 ",
    'rect': "🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿 ",
    'rect-bold': "🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉0123456789 ",
    'script': "𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫 ",
    'script-bold': "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝓌𝓍𝓎𝓏𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫 ",
    'small-caps': "ABCDEFGHIJKLMNOPQRSTUVWXYZᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫 ",
    'censored': "███████████████████████████████████████████████████████████████",
    'slack': [
        f"{W}a:", f"{W}b:", f"{W}c:", f"{W}d:", f"{W}e:", f"{W}f:", f"{W}g:", f"{W}h:", f"{W}i:", f"{W}j:", f"{W}k:",
        f"{W}l:", f"{W}m:", f"{W}n:", f"{W}o:", f"{W}p:", f"{W}q:", f"{W}r:", f"{W}s:", f"{W}t:", f"{W}u:", f"{W}v:",
        f"{W}w:", f"{W}x:", f"{W}y:", f"{W}z:", f"{W}a:", f"{W}b:", f"{W}c:", f"{W}d:", f"{W}e:", f"{W}f:", f"{W}g:",
        f"{W}h:", f"{W}i:", f"{W}j:", f"{W}k:", f"{W}l:", f"{W}m:", f"{W}n:", f"{W}o:", f"{W}p:", f"{W}q:", f"{W}r:",
        f"{W}s:", f"{W}t:", f"{W}u:", f"{W}v:", f"{W}w:", f"{W}x:", f"{W}y:", f"{W}z:",
        ":zero:", ":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:",
        "   ",
    ],
    'slack-yellow': [
        f"{Y}a:", f"{Y}b:", f"{Y}c:", f"{Y}d:", f"{Y}e:", f"{Y}f:", f"{Y}g:", f"{Y}h:", f"{Y}i:", f"{Y}j:", f"{Y}k:",
        f"{Y}l:", f"{Y}m:", f"{Y}n:", f"{Y}o:", f"{Y}p:", f"{Y}q:", f"{Y}r:", f"{Y}s:", f"{Y}t:", f"{Y}u:", f"{Y}v:",
        f"{Y}w:", f"{Y}x:", f"{Y}y:", f"{Y}z:", f"{Y}a:", f"{Y}b:", f"{Y}c:", f"{Y}d:", f"{Y}e:", f"{Y}f:", f"{Y}g:",
        f"{Y}h:", f"{Y}i:", f"{Y}j:", f"{Y}k:", f"{Y}l:", f"{Y}m:", f"{Y}n:", f"{Y}o:", f"{Y}p:", f"{Y}q:", f"{Y}r:",
        f"{Y}s:", f"{Y}t:", f"{Y}u:", f"{Y}v:", f"{Y}w:", f"{Y}x:", f"{Y}y:", f"{Y}z:",
        ":zero:", ":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:",
        "   ",
    ],
}


def term_color(r, g, b):
    r = round(max(0.0, min(5.0, r * 6.0)))
    g = round(max(0.0, min(5.0, g * 6.0)))
    b = round(max(0.0, min(5.0, b * 6.0)))

    return int(16 + r + g * 6 + b * 6 * 6)


def hsv(index, length):
    # rainbow
    bucket_size = length / 6.0
    index_in_bucket = index / bucket_size - math.floor(index / bucket_size)

    # r1, g+, b0
    if index < bucket_size:
        r = 1.0
        g = index_in_bucket
        b = 0.0

    # r-, g1, b0
    elif index < 2 * bucket_size:
        r = 1.0 - index_in_bucket
        g = 1.0
        b = 0.0

    # r0, g1, b+
    elif index < 3 * bucket_size:
        r = 0.0
        g = 1.0
        b = index_in_bucket

    # r0, g-, b1
    elif index < 4 * bucket_size:
        r = 0.0
        g = 1.0 - index_in_bucket
        b = 1.0

    # r+, g0, b1
    elif index < 5 * bucket_size:
        r = index_in_bucket
        g = 0.0
        b = 1.0

    # r+, g0, b-
    else:  # index < 6 * bucket_size
        r = 1.0
        g = 0.0
        b = 1.0 - index_in_bucket

    return term_color(r, g, b)


def rainbowify(message):
    return "".join(
        list(
            map(
                lambda a:
                f"\033[38;5;{hsv(a[0], len(message))}m{a[1]}\033[m",
                enumerate(message)
            )
        )
    )


def index_in_font(c: str) -> int | None:
    if c.isalpha():
        if c.isupper():
            return ord(c) - ord('A')
        else:
            return ord(c) - ord('a') + 26
    elif c.isdigit():
        return -(1 + 10 - int(c))
    elif c.isspace():
        return -1
    else:
        return None


def fraktur(message, font):
    out = ''
    if font in fonts:
        for c in message:
            index = index_in_font(c)
            if index:
                out += fonts[font][index]
            else:
                out += c
    else:
        out = f"Font '{font}' not found."
    return out


def fraktur_all(message, selected_fonts=None, with_name=False, colorized=False):
    if selected_fonts is None:
        selected_fonts = list(fonts.keys())

    for font in sorted(selected_fonts):
        result = fraktur(message, font)
        if colorized:
            result = "".join(rainbowify(result))

        if with_name:
            print(f"{font}: {result}")
        else:
            print(result)


def generate(message: str, font: str = None, with_name: bool = False, rainbowify: bool = False):
    if not font:
        fraktur_all(message, ['fraktur'], with_name, rainbowify)
    else:
        if font == 'all':
            fraktur_all(message, list(fonts.keys()), with_name, rainbowify)
        else:
            if font in fonts:
                fraktur_all(message, [font], with_name, rainbowify)
            else:
                found_fonts = list(filter(lambda x: x.lower().find(font.lower()) > -1, fonts.keys()))
                if len(found_fonts) > 0:
                    fraktur_all(message, found_fonts, with_name, rainbowify)
                else:
                    print(f"Font {font} not found.")


def main():
    import sys

    if len(sys.argv) == 2:
        generate(message=sys.argv[1])
    elif len(sys.argv) == 3:
        generate(message=sys.argv[1], font=sys.argv[2])
    elif len(sys.argv) == 4:
        generate(message=sys.argv[1], font=sys.argv[2], with_name=sys.argv[3].lower() == 'true')
    elif len(sys.argv) == 5:
        generate(message=sys.argv[1], font=sys.argv[2], with_name=sys.argv[3].lower() == 'true',
                 rainbowify=sys.argv[4].lower() == 'true')
    else:
        print(
            f"Usage: {sys.argv[0]} [MESSAGE [FONT [WITH_NAME [RAINBOWIFY]]]]\n\n"
            f"MESSAGE:\tsome text\n"
            f"FONT:\t\t{', '.join(sorted(list(fonts.keys())))}\n"
            f"\t\tor 'all' for all fonts\n"
            f"\t\tor partial match\n"
            f"WITH_NAME:\t'True' for enabling printing of names.\n"
            f"RAINBOWIFY:\t'True' for enabling colorization of fonts."
        )


if __name__ == "__main__":
    main()
