from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
нєу {}.
ωєℓ¢σмє тσ {}

ι αм тнє мαѕтєя σƒ ωнιѕρєяєяѕ мєѕѕαgєѕ мєαηѕ уσυ ¢αη ѕнαяє нι∂∂єη мєѕѕαgє тσ αηуσηє .

уσυ ¢αη υѕє мє тσ ѕєη∂ ωнιѕρєяѕ тσ уσυя ƒяιєη∂ ιη gяσυρѕ αη∂ ¢нαηηєℓѕ (єνєη ιƒ ι'м ησт тнєяє).
σηℓу тнαт ƒяιєη∂ αη∂ уσυ ωιℓℓ вє αвℓє тσ яєα∂ тнє мєѕѕαgє єνєη тнσυgн σтнєяѕ αяє ιη ѕαмє gяσυρ. 

тσ ѕєє нσω тσ υѕє мє ρяєѕѕ 'нσω тσ υѕє' вєℓσω.

ву @GORILLA_NETWORKS
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔒 ѕєη∂ α ωнιѕρєя 🔒", switch_inline_query="")],
        [InlineKeyboardButton(text="🏠 яєтυη нσмє 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔒 ѕєη∂ α ωнιѕρєя 🔒", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("нσω тσ υѕє ❔", callback_data="help"),
            InlineKeyboardButton("🎪 αвσυт 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ вσт ѕυρρσят ♥", url="https://t.me/GORILLA_BOTS")],
        [InlineKeyboardButton("🎨 ηєтωσяк 🎨", url="https://t.me/GORILLA_NETWORK")],
    ]

    # Help Message
    HELP = """
    נυѕт туρє тнє мєѕѕαgє ιη вєℓσω ƒσямαт ιη αηу ¢нαт.
    єχαмρℓє :- @ωg_gвσт нєℓℓσ тнιѕ ιѕ вℓα¢кмαмвα @мαмвα_яєтυяηѕ

`@ωg_gвσт уσυя_мєѕѕαgє ƒяιєη∂_υѕєяηαмє/ι∂`
    """

    # αвσυт мєѕѕαgє
    αвσυт = """
**αвσυт тнιѕ вσт**

вσт ¢яєαтє∂ ву @GORILLA_NETWORK

ѕσυя¢є ¢σ∂є : [¢ℓι¢к нєяє](https://github.com/FantasticSukhi/WhisperBot)

ιηѕριяє∂ ву : nnbbot

ƒяαмєωσяк : [ρуяσgяαм](docs.pyrogram.org)

ℓαηgυαgє : [ρутнση](www.python.org)

∂єνєℓσρєя : @MAMBA_RETURNS
    
