# dev by envy
import discord
from discord.ext import commands
from discord import app_commands, Interaction, SelectOption
from discord import ui
from discord.ui import (
    LayoutView,
    Container,
    TextDisplay,
    Separator,
    ActionRow,
    Select,
)

TOKEN = "token"
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="$", intents=intents)


# data containers
def build_service_container(title: str, items: list[tuple[str, str]]) -> Container:
    container = Container(accent_color=None)
    container.add_item(TextDisplay(f"## {title}"))
    container.add_item(Separator())
    
    content = []
    for name, price in items:
        content.append(f"> **• {name}:**\n> ```\n> {price}\n> ```")
    
    container.add_item(TextDisplay("\n\n".join(content)))
    container.add_item(Separator())
    container.add_item(TextDisplay("-# Chọn dịch vụ khác trong menu bên dưới để xem thêm."))
    return container


def build_error_container() -> Container:
    container = Container(accent_color=None)
    container.add_item(TextDisplay("## ❌ KHÔNG THỂ THAO TÁC"))
    container.add_item(Separator())
    container.add_item(TextDisplay("Bạn không phải người dùng lệnh này. Vui lòng tự gõ `/menu` để sử dụng dịch vụ!"))
    return container


def get_container(key: str) -> Container:
    if key == "TikTok":
        return build_service_container(
            "<a:Tiktok:1536209502473429072> Tăng Tương Tác TikTok",
            [
                ("Buff Tim TikTok", "Giá: 25k/1k Tim (Min 100)"),
                ("Buff Theo Dõi TikTok", "Giá: 55k/1k TD (Min 50)"),
                ("Buff View TikTok", "Giá: 5k/1k View (Min 100)"),
                ("Buff Share Video TikTok", "Giá: 3,6k/1k Share (Min 10)"),
                ("Buff Bình Luận TikTok", "Giá: 125k/1k Bình Luận có nội dung (Min 10)"),
                ("Buff Lưu Video TikTok", "Giá: 55,5k/100k Lưu Video (Min 10)"),
                ("Buff Mắt Xem Live", "Giá: 43k/100 Mắt Xem Live (Có thể lựa chọn time) (Min 10)"),
            ]
        )
    elif key == "Instagram":
        return build_service_container(
            "<a:Ig:1536211164298481704> Tăng Tương Tác Instagram",
            [
                ("Buff Theo Dõi Instagram", "Giá: 15k/1k Theo Dõi (Min 100)"),
                ("Buff Like Instagram", "Giá: 23k/10k Like (Min 10)"),
                ("Buff Chia Sẻ Instagram", "Giá: 11,5k/10k Chia Sẻ (Min 100)"),
                ("Buff View Instagram", "Giá: 12,5k/100k View (Min 100)"),
                ("Buff Bình Luận Instagram", "Giá: 21,5k/1k Bình Luận có nội dung (Min 100)"),
                ("Buff Views Story Instagram", "Giá: 12,5k/1k Views Story (Min 10)"),
            ]
        )
    elif key == "Facebook":
        return build_service_container(
            "<a:Facebook:1536209201376796702> Tăng Tương Tác Facebook",
            [
                ("Buff Theo Dõi Facebook", "Giá: 22,5k/1k Theo Dõi (Min 10)"),
                ("Buff Bình Luận Facebook", "Giá: 180k/1k Bình Luận có nội dung (Min 10)"),
                ("Buff View Video Facebook", "Giá: 21,5k/10k View Video (Min 500)"),
                ("Buff View Reels Facebook", "Giá: 21,5k/10k View Reels (Min 500)"),
                ("Buff Thả Cảm Xúc Facebook", "Giá: 17k/1k Thả Cảm Xúc (Min 30)"),
                ("Buff View Story Facebook", "Giá: 14k/1k View Story (Min 100)"),
                ("Buff Thành Viên Group Facebook", "Giá: 15k/1k Thành Viên (Min 100)"),
                ("Buff Like Profile/Page Facebook", "Giá: 85k/50 Like (Tăng 5 Bài) (Min 50)"),
                ("Buff Chia Sẻ Facebook", "Giá: 13,5k/10k Chia Sẻ (Min 100)"),
            ]
        )
    elif key == "YouTube":
        return build_service_container(
            "<a:Youtube:1536209219328540672> Tăng Tương Tác YouTube",
            [
                ("Buff Like YouTube", "Giá: 100k/1k Like (Min 10)"),
                ("Buff Sub YouTube", "Giá: 43,5k/1k Sub (Min 10)"),
                ("Buff View YouTube", "Giá: 82k/1k View (Min 100)"),
                ("Buff Mắt Live YouTube", "Giá: 6,7k/1k Mắt Live (Min 100)"),
                ("Buff Bình Luận", "Giá: 210k/1k Bình Luận (Max 50k)"),
                ("Buff Like Bình Luận", "Giá: 14,5k/1k Like Bình Luận (Min 10)"),
            ]
        )
    elif key == "Telegram":
        return build_service_container(
            "<a:Telegram:1536209223841742898> Tăng Tương Tác Telegram",
            [
                ("Buff Thành Viên Group", "Giá: 23k/1k Thành Viên (Min 10)"),
            ]
        )
    elif key == "Threads":
        return build_service_container(
            "<a:Threads:1536209230367825981> Tăng Tương Tác Threads",
            [
                ("Buff Like Threads", "Giá: 94k/1k Like (Min 50)"),
                ("Buff Follow Threads", "Giá: 124k/1k Follows (Min 50)"),
                ("Buff Comments Threads", "Giá: 350k/100 Comments (Min 100)"),
            ]
        )
    elif key == "Shopee":
        return build_service_container(
            "<a:Shoppe:1536209237288554516> Tăng Tương Tác Shopee",
            [
                ("Buff Theo Dõi Shopee", "Giá: 36k/100 Theo Dõi (Min 50)"),
                ("Buff Like Shopee", "Giá: 20k/100k Like (Min 50)"),
            ]
        )
    elif key == "App X":
        return build_service_container(
            "<a:X_:1536209245853188146> Tăng Tương Tác App X",
            [
                ("Buff Theo Dõi App X", "Giá: 183k/100 Theo Dõi (Min 10)"),
                ("Buff View App X", "Giá: 62k/1k View (Min 100)"),
            ]
        )
    elif key == "Owo":
        return build_service_container(
            "<:Owo:1536283179051126885> Thu/Mua Cowoncy",
            [
                ("Giá Thu Cowoncy", "Giá: 5k->7k/1M (Min 1M)"),
                ("Giá Bán Cowoncy", "Giá: 10k/1M (Min 1M)"),
            ]
        )
    elif key == "Tài Nguyên MMO 1":
        return build_service_container(
            "<a:Tick_1:1536288530546950144> Tài Nguyên MMO (Phần 1)",
            [
                ("Gemini Veo3 Pro1", "Tạo Ticket Để Được Tư Vấn"),
                ("Grok 10$/50$/100$/200$/Super Grok 3M", "Tạo Ticket Để Được Tư Vấn"),
                ("Netflix Premium 4K+ 1M", "Tạo Ticket Để Được Tư Vấn"),
                ("Capcut Pro 30D/7D/Pro Personal 6M", "Tạo Ticket Để Được Tư Vấn"),
                ("Youtube Premium 1M/3M/6M/12M", "Tạo Ticket Để Được Tư Vấn"),
                ("Youtube Premium Slot 3M/6M/12M", "Tạo Ticket Để Được Tư Vấn"),
                ("CD KEY 9 PROXY 100IP/200IP", "Tạo Ticket Để Được Tư Vấn"),
                ("Canva Edu Pro Personal Upgrade 3M/6M/12M", "Tạo Ticket Để Được Tư Vấn"),
                ("Canva Pro Nonprofits Premium Plan 1M/3M/6M/12M", "Tạo Ticket Để Được Tư Vấn"),
                ("Claude 10$/30$/50$/100$", "Tạo Ticket Để Được Tư Vấn"),
                ("Claude Pro Team Add 1M", "Tạo Ticket Để Được Tư Vấn"),
                ("Avast SecureLine VPN 1M", "Tạo Ticket Để Được Tư Vấn"),
                ("ExpressVPN Full 3->7D", "Tạo Ticket Để Được Tư Vấn"),
                ("HMA VPN 5 DEVICES 12M (PC/ANDROID/IPHONE)", "Tạo Ticket Để Được Tư Vấn"),
                ("HMA VPN 5 DEVICES 28D->30D (PC/ANDROID/IPHONE)", "Tạo Ticket Để Được Tư Vấn"),
                ("HMA VPN 5 DEVICES 28->30D (PC/ANDROID)", "Tạo Ticket Để Được Tư Vấn"),
                ("HMA VPN 20 DEVICES 12M (PC/ANDROID/IPHONE)", "Tạo Ticket Để Được Tư Vấn"),
                ("NorsVPN Premium 1Y 7/20 DEVICES", "Tạo Ticket Để Được Tư Vấn"),
                ("Proton VPN 25D 1/10 DEVICES", "Tạo Ticket Để Được Tư Vấn"),
                ("Surfshark VPN 7D", "Tạo Ticket Để Được Tư Vấn"),
            ]
        )
    elif key == "Tài Nguyên MMO 2":
        return build_service_container(
            "<a:Tick_1:1536288530546950144> Tài Nguyên MMO (Phần 2)",
            [
                ("Cursor 30D 700/1K3/2k6/6K5/13k Request", "Tạo Ticket Để Được Tư Vấn"),
                ("Cursor 3D/7D", "Tạo Ticket Để Được Tư Vấn"),
                ("Doulingo Super 1Y", "Tạo Ticket Để Được Tư Vấn"),
                ("GPM Login Key Lincense 1M/LifeTime", "Tạo Ticket Để Được Tư Vấn"),
                ("Gamma Ultra 1M", "Tạo Ticket Để Được Tư Vấn"),
                ("Gemini Veo Sell All", "Tạo Ticket Để Được Tư Vấn"),
                ("Gemini Pro CC 18M + Google Drive", "Tạo Ticket Để Được Tư Vấn"),
                ("Google 1Y 5TB/30TB", "Tạo Ticket Để Được Tư Vấn"),
                ("MS365 Premium Admin 7M 1TB 5 Slots", "Tạo Ticket Để Được Tư Vấn"),
                ("Roboneo 150 Use Kling Motion 3.0, Seedance 2.0", "Tạo Ticket Để Được Tư Vấn"),
                ("HeyGen Creator $29 FW25D", "Tạo Ticket Để Được Tư Vấn"),
                ("Gmail 200X->2019 @gmail.com", "Tạo Ticket Để Được Tư Vấn"),
                ("Hotmail Trusted (GraphAPI) 6->12M Skip 7D Fresh Account", "Tạo Ticket Để Được Tư Vấn"),
                ("Outlook Trusted (GraphAPI) 6->12M Skip 7D Fresh Account", "Tạo Ticket Để Được Tư Vấn"),
                ("Locket Gold LifeTime", "Tạo Ticket Để Được Tư Vấn"),
                ("Microsoft 365 Premium Family Add 6M/1Y", "Tạo Ticket Để Được Tư Vấn"),
                ("Shoppe Account Aged 5M (New User Code Ready)", "Tạo Ticket Để Được Tư Vấn"),
                ("Tiktok Aged Cart Enbled (Live Enbled)", "Tạo Ticket Để Được Tư Vấn"),
                ("XBOX GIFT CODE - RANDOM", "Tạo Ticket Để Được Tư Vấn"),
                ("Hotmail Outlook Trust", "Tạo Ticket Để Được Tư Vấn"),
            ]
        )
    elif key == "Tài Nguyên MMO 3":
        return build_service_container(
            "<a:Tick_1:1536288530546950144> Tài Nguyên MMO (Phần 3)",
            [
                ("Zoom Pro 14D/28D", "Tạo Ticket Để Được Tư Vấn"),
                ("ElevenLabs 10K Credit", "Tạo Ticket Để Được Tư Vấn"),
                ("ElevenLabs Creator 1M", "Tạo Ticket Để Được Tư Vấn"),
                ("Meitu SVIP 1Y 1 Device 1M/1Y", "Tạo Ticket Để Được Tư Vấn"),
                ("Meitu Vip 7D", "Tạo Ticket Để Được Tư Vấn"),
                ("Wink SVIP 28D 1 Device", "Tạo Ticket Để Được Tư Vấn"),
                ("Wink Vip +7D", "Tạo Ticket Để Được Tư Vấn"),
                ("Artlist 240k Credit", "Tạo Ticket Để Được Tư Vấn"),
                ("OpenArt Wonder $240 106K Credits", "Tạo Ticket Để Được Tư Vấn"),
                ("Api Cursor 30D 30.000 Request", "Tạo Ticket Để Được Tư Vấn"),
                ("Cloud VPS 1-1-20 1M", "Tạo Ticket Để Được Tư Vấn"),
                ("Cloud VPS 1-2-25 1M", "Tạo Ticket Để Được Tư Vấn"),
                ("Cloud VPS 16-32-100 1M", "Tạo Ticket Để Được Tư Vấn"),
                ("Cloud VPS 2-4-30 1M", "Tạo Ticket Để Được Tư Vấn"),
                ("Cloud VPN 4-8-50 1M", "Tạo Ticket Để Được Tư Vấn"),
                ("Cloud VPN 8-16-70 1M", "Tạo Ticket Để Được Tư Vấn"),
                ("Codex 150$ Dùng Trong 7D", "Tạo Ticket Để Được Tư Vấn"),
                ("Codex Ai 10$/50$/100$/200$/500$", "Tạo Ticket Để Được Tư Vấn"),
                ("Gemini Veo3 Pro1 1Y 5TB (Mail Trâu)", "Tạo Ticket Để Được Tư Vấn"),
                ("Sell Via Facebook USA...", "Tạo Ticket Để Được Tư Vấn"),
                ("Chat GPT Plus/Pro Business", "Tạo Ticket Để Được Tư Vấn"),
            ]
        )
    elif key == "Tricker Facebook":
        return build_service_container(
            "<a:Tick_1:1536288530546950144> Tricker Facebook",
            [
                ("Tut Back Acc Facebook", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Đổi Mật Khẩu FB Cho Via Không Cần CC", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Đổi Ngày Tháng Năm Sinh Không GH", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Đổi Tên Facebook Trước 60D", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Kháng Bản Quyền Facebook", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Kick Thiết Bị Lạ", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Unlock Acc Facebook 282", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Unlock Acc Facebook 956", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Verify Bảo Vệ Acc FB", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Xác Minh Danh Tính Mess Selfie", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Xóa Rip + Scripr Rip Fb", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Dame Facebook", "Tạo Ticket Để Được Tư Vấn"),
                ("Tool Auto Dame Facebook", "Tạo Ticket Để Được Tư Vấn"),
            ]
        )
    elif key == "Tricker Tiktok":
        return build_service_container(
            "<a:Tick_1:1536288530546950144> Tricker Tiktok",
            [
                ("Tut Dame Live Tiktok", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Dame Video", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Fix Hạn Chế Live 30s", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Fix Lỗi Mở Live Tiktok", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Kháng Cmt Bị VP", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Kháng Giới Giạn Độ Tuổi", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Kháng Hồ Sờ Đình Chỉ", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Kháng Livestream Tiktok", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Kháng VD Tiktok", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Rửa IP Thiết Bị Khi Bị Flag", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Lấy Lại Acc Bị Hack", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Up Acc Doanh Nghiệp", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Mở Cấm Chat", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Mở Khóa Dạng Mạo Tiktok", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Mở Shop Tiktok", "Tạo Ticket Để Được Tư Vấn"),
                ("Tut Xây Kênh Tiktok", "Tạo Ticket Để Được Tư Vấn"),
                ("Tool Auto Dame Tiktok", "Tạo Ticket Để Được Tư Vấn"),
            ]
        )
    elif key == "Dịch Vụ Mạng Xã Hội":
        return build_service_container(
            "<a:Tick_1:1536288530546950144> Dịch Vụ Mạng Xã Hội",
            [
                ("Dame Tiktok", "Tạo Ticket Để Được Tư Vấn"),
                ("Dame Facebook", "Tạo Ticket Để Được Tư Vấn"),
                ("Dame Instagram", "Tạo Ticket Để Được Tư Vấn"),
                ("Unlock Ban 282 Facebook", "Tạo Ticket Để Được Tư Vấn"),
                ("Unlock Ban 956 Facebook", "Tạo Ticket Để Được Tư Vấn"),
                ("Unlock Ban Live Tiktok", "Tạo Ticket Để Được Tư Vấn"),
                ("Mở Giỏ Hàng Tiktok", "Tạo Ticket Để Được Tư Vấn"),
                ("Tài Khoản Tiktok Đã Xây Sẵn", "Tạo Ticket Để Được Tư Vấn"),
                ("Dạy Dame Các Nền Tảng Mỗi Nền Tảng 1 Kèm 1", "7 Triệu 2 /1NT"),
                ("Nhận Lên Tick Xanh Tiktok Và Các Roles Khác", "Tạo Ticket Để Được Tư Vấn"),
                ("Nhận Lên Tick Xanh Facebook", "Tạo Ticket Để Được Tư Vấn"),
                ("Làm Mọi Thứ Có Thể Làm", "Tạo Ticket Để Được Tư Vấn"),
            ]
        )
    elif key == "Dịch Vụ Code Bot":
        return build_service_container(
            "<a:Tick_1:1536288530546950144> Dịch Vụ Code Bot",
            [
                ("Nhận Code Bot Telegram/Discord/Zalo", "Tạo Ticket Để Được Tư Vấn"),
                ("Nhận Code Tool Telegram/Discord/Zalo", "Tạo Ticket Để Được Tư Vấn"),
                ("Nhận Code Tool Theo Yêu Cầu", "Tạo Ticket Để Được Tư Vấn"),
                ("Nhận Code Website Theo Yêu Cầu", "Tạo Ticket Để Được Tư Vấn"),
            ]
        )
    elif key == "Dịch Vụ Bán Tên Miền Website":
        return build_service_container(
            "<a:Tick_1:1536288530546950144> Dịch Vụ Bán Tên Miền Website",
            [
                ("Com", "Tạo Ticket Để Được Tư Vấn"),
                ("Org", "Tạo Ticket Để Được Tư Vấn"),
                ("Site", "Tạo Ticket Để Được Tư Vấn"),
                ("Vn", "Tạo Ticket Để Được Tư Vấn"),
                ("Edu", "Tạo Ticket Để Được Tư Vấn"),
                ("Shop", "Tạo Ticket Để Được Tư Vấn"),
                ("Bet", "Tạo Ticket Để Được Tư Vấn"),
                ("Net", "Tạo Ticket Để Được Tư Vấn"),
                ("Tất Cả Bán Theo Năm Có Bán Tên Miền Có Sẵn", "Tạo Ticket Để Được Tư Vấn"),
            ]
        )
    
    # mặc định main menu
    default_container = Container(accent_color=None)
    default_container.add_item(TextDisplay("## 📋 MENU BẢNG GIÁ DỊCH VỤ"))
    default_container.add_item(Separator())
    default_container.add_item(TextDisplay("Vui lòng chọn dịch vụ trong menu bên dưới để xem chi tiết."))
    return default_container


SERVICE_KEYS = [
    ("TikTok", "1536209502473429072"),
    ("Instagram", "1536211164298481704"),
    ("Facebook", "1536209201376796702"),
    ("YouTube", "1536209219328540672"),
    ("Telegram", "1536209223841742898"),
    ("Threads", "1536209230367825981"),
    ("Shopee", "1536209237288554516"),
    ("App X", "1536209245853188146"),
    ("Owo", "1536283179051126885"),
    ("Tài Nguyên MMO 1", "1536288530546950144"),
    ("Tài Nguyên MMO 2", "1536288530546950144"),
    ("Tài Nguyên MMO 3", "1536288530546950144"),
    ("Tricker Facebook", "1536288530546950144"),
    ("Tricker Tiktok", "1536288530546950144"),
    ("Dịch Vụ Mạng Xã Hội", "1536288530546950144"),
    ("Dịch Vụ Code Bot", "1536288530546950144"),
    ("Dịch Vụ Bán Tên Miền Website", "1536288530546950144"),
]


# layout views
class ErrorLayoutView(LayoutView):
    def __init__(self):
        super().__init__()
        self.add_item(build_error_container())


class DynamicDetailLayoutView(LayoutView):
    def __init__(self, selected_key: str):
        super().__init__(timeout=200.0)
        
        container = get_container(selected_key)
        
        self.dropdown = Select(
            placeholder="Chọn dịch vụ khác...",
            min_values=1,
            max_values=1,
            options=[
                SelectOption(
                    label=name,
                    value=name,
                    description=f"Xem bảng giá {name}",
                    emoji=discord.PartialEmoji(name=name, id=int(emoji_id)),
                    default=(name == selected_key)
                ) for name, emoji_id in SERVICE_KEYS
            ]
        )
        self.dropdown.callback = self.on_select_change
        container.add_item(ActionRow(self.dropdown))
        
        self.add_item(container)

    async def on_select_change(self, interaction: Interaction):
        selected_key = interaction.data["values"][0]
        new_view = DynamicDetailLayoutView(selected_key)
        await interaction.response.edit_message(view=new_view)

    async def on_timeout(self):
        self.dropdown.disabled = True
        try:
            await self.message.edit(view=self)
        except Exception:
            pass


class MainMenuView(LayoutView):
    def __init__(self, author_id: int = None):
        super().__init__(timeout=None)
        self.author_id = author_id
        
        container = get_container("main")
        
        dropdown = Select(
            custom_id="persistent_linodz_menu_select",
            placeholder="Chọn dịch vụ...",
            min_values=1,
            max_values=1,
            options=[
                SelectOption(
                    label=name,
                    value=name,
                    description=f"Xem bảng giá {name}",
                    emoji=discord.PartialEmoji(name=name, id=int(emoji_id))
                ) for name, emoji_id in SERVICE_KEYS
            ]
        )
        dropdown.callback = self.on_dropdown_select
        container.add_item(ActionRow(dropdown))
        
        self.add_item(container)

    async def on_dropdown_select(self, interaction: Interaction):
        # kiểm tra nếu người bấm không phải người đã gọi lệnh
        if self.author_id and interaction.user.id != self.author_id:
            await interaction.response.send_message(
                view=ErrorLayoutView(),
                ephemeral=True
            )
            return

        selected_key = interaction.data["values"][0]
        detail_view = DynamicDetailLayoutView(selected_key)
        
        await interaction.response.send_message(
            view=detail_view,
            ephemeral=True
        )


# bot events & commands
@bot.event
async def on_ready():
    bot.add_view(MainMenuView())
    await bot.tree.sync()
    print(f"Logged in as: {bot.user}")


@bot.tree.command(name="menu", description="Mở menu bảng giá dịch vụ")
async def menu(interaction: Interaction):
    view = MainMenuView(author_id=interaction.user.id)
    await interaction.response.send_message(view=view)


bot.run(TOKEN)
