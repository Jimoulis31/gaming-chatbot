from sentence_transformers import SentenceTransformer, util
import tkinter as tk
from tkinter import scrolledtext

model = SentenceTransformer('all-MiniLM-L6-v2')
qa_pairs = [
    # --- GREETINGS / GENERAL ---
    ("hello hi hey greetings yo sup", "Hey! What are you trying to get into today — games, builds, or fixes?"),
    ("thanks thank you appreciate ty", "No problem! If you need more help with games or your setup, just ask."),

    # --- GAME RECOMMENDATIONS ---
    ("recommend game suggestion what should i play pc console",
     "Tell me your mood + platform (PC/PS/Xbox/Switch). I'll give you some solid picks."),
    ("best games 2025 2026 new releases recent top rated",
     "Top recent picks: Clair Obscur: Expedition 33, Black Myth: Wukong, Split Fiction, Elden Ring Nightreign, and Nioh 3."),

    # --- GENRES ---
    ("fps first person shooter shooter call of duty valorant cs2",
     "FPS picks: Valorant (tactical), CS2 (classic competitive), Apex Legends (fast movement), CoD (casual + polished). ARC Raiders is a promising new co-op shooter in 2026."),
    ("rpg role playing game elden ring witcher skyrim baldurs gate metaphor",
     "Top RPGs: Elden Ring Nightreign (co-op roguelike), Baldur's Gate 3 (choice-based), Clair Obscur: Expedition 33 (turn-based, stunning), Metaphor: ReFantazio (JRPG gem)."),
    ("open world gta rdr2 cyberpunk sandbox explore crimson desert",
     "Open world: RDR2 (immersion king), Cyberpunk 2077 (story + visuals), Crimson Desert (2026 action-RPG), GTA VI is console-first in late 2026 with PC TBD."),
    ("strategy rts turn based civilization starcraft age of empires",
     "Strategy: Civ VII (just released), AoE IV (real-time), StarCraft II (still the competitive RTS standard)."),
    ("horror survival scary game resident evil silent hill alan wake",
     "Horror picks: Silent Hill F (2025, critically acclaimed), Resident Evil Requiem (upcoming), Alan Wake 2 (psychological), Lethal Company (co-op chaos)."),
    ("indie small game hades hollow knight stardew celeste balatro blue prince",
     "Indie gems: Hades II (early access, excellent), Balatro (card roguelike, huge), Blue Prince (2025 puzzle hit), Hollow Knight: Silksong (still coming), Stardew Valley (timeless)."),
    ("multiplayer co op friends online party games split fiction",
     "Co-op fun: Split Fiction (best co-op of 2025), Helldivers 2, Deep Rock Galactic, It Takes Two, Sea of Thieves, ARC Raiders."),
    ("single player story narrative cinematic game",
     "Story-driven: Clair Obscur: Expedition 33 (2025 GOTY contender), The Last of Us Part I/II PC, God of War, Red Dead Redemption 2, Disco Elysium."),

    # --- PLATFORMS ---
    ("pc gaming setup build hardware parts upgrade",
     "GPU first, then CPU, then RAM. In 2026, RTX 5070 or RX 9070 XT for 1440p. Tell me your budget and I'll help you build."),
    ("console playstation xbox nintendo switch which to buy",
     "PS5 = exclusives + DualSense feel, Xbox = Game Pass value, Switch 2 = portable + Nintendo exclusives. Switch 2 launched in 2025."),
    ("ps5 playstation 5 exclusives sony games",
     "PS5 highlights: Spider-Man 2, God of War Ragnarök, Stellar Blade, and upcoming exclusives. Still the console to beat for exclusives."),
    ("xbox series x microsoft game pass exclusives",
     "Xbox shines with Game Pass (day-one releases included), Halo, Forza Horizon, and strong backwards compatibility."),
    ("nintendo switch 2 zelda mario pokemon exclusives",
     "Switch 2 must-plays: next mainline Zelda, Mario Kart World, and Pokémon Pokopia — a cozy life sim praised as Animal Crossing meets Dragon Quest Builders."),

    # --- PERFORMANCE / TECH FIXES ---
    ("lag fps low performance stutter frames drop",
     "Fix FPS drops: update GPU drivers, lower shadow quality, close background apps, enable DLSS 4 (Nvidia) or FSR 3.1 / FSR Redstone (AMD) if available."),
    ("game not launching crashing error fix",
     "Try: verify game files on Steam, update GPU drivers, reinstall VC++ redistributables, and disable overlays (Discord, GeForce Experience)."),
    ("overheating thermal throttling gaming laptop heat",
     "Fix heat: clean fans, improve airflow, use a balanced power mode, and consider repasting the CPU/GPU if temps are above 95°C."),

    # --- HARDWARE ---
    ("gpu graphics card upgrade nvidia amd best 2025 2026",
     "Top 1440p GPUs in 2026: RTX 5070 (DLSS 4, 12GB GDDR7) and RX 9070 XT (16GB GDDR6, great value). The RX 9070 XT often beats the RTX 5070 in rasterization at a lower price."),
    ("cpu processor gaming ryzen intel best 2025 2026",
     "Best gaming CPU in 2026 is the AMD Ryzen 7 9800X3D — its massive 3D V-Cache dominates frame rates, beating Intel's best by 15–35% in gaming. The 9850X3D is marginally faster but costs more."),
    ("ram memory how much gaming ddr5 ddr4",
     "32GB DDR5-6000 CL30 is the sweet spot in 2026. 16GB is still the minimum but some AAA games push past it. Enable EXPO (AMD) or XMP (Intel) in BIOS for full speed."),
    ("monitor refresh rate resolution hz 1440p 1080p 4k",
     "1440p at 144–180Hz is the sweet spot for most gamers. 1080p is still great for esports at 240Hz+. 4K suits high-end rigs with an RTX 5080 or above."),
    ("keyboard mouse controller input gaming setup",
     "KBM = precision (FPS/strategy), controller = comfort (racing, action, sports). Most PC games support both in 2026."),

    # --- PLATFORMS / STORES / SUBSCRIPTIONS ---
    ("steam epic games store where to buy games gog",
     "Steam = best library + community + sales. Epic = weekly free games + some exclusives. GOG = DRM-free classics. Most players use Steam as their primary store."),
    ("game pass xbox subscription worth it",
     "Game Pass is still one of the best deals in gaming: huge library + Xbox exclusives on day one + PC Game Pass available."),
    ("ps plus playstation plus subscription benefits",
     "PS Plus gives online play, monthly free games, and a game catalog depending on your tier (Essential / Extra / Premium)."),
    ("game sale discount cheap deal steam epic humble",
     "Best deals: Steam seasonal sales (Summer/Winter), Epic weekly freebies, Humble Bundle packs, and Fanatical bundles."),

    # --- COMPETITIVE / ESPORTS ---
    ("rank ranked competitive matchmaking improve climb",
     "Improve rank: focus on one role or champion, learn core fundamentals, review your replays, and keep session length consistent to avoid tilt."),
    ("cheater hacker anti cheat report toxic players",
     "Report and move on. Don't tilt — every game you focus on your own play is a game you improve. Most titles have improved anti-cheat in 2025–2026."),
    ("esports tournament pro player competitive gaming",
     "Top esports in 2026: CS2, Valorant, League of Legends, Dota 2 — all with massive prize pools and global pro scenes."),

    # --- SPECIFIC GAMES ---
    ("minecraft sandbox survival building mods",
     "Minecraft remains massive in 2026 — survival, creative, massive mod ecosystems, and servers. Still one of the best-selling games of all time."),
    ("fortnite battle royale building zero build",
     "Fortnite evolves constantly. Zero Build is great for casual play; building mode has a higher skill ceiling. Collaborations and new chapters keep it fresh."),
    ("league of legends lol moba ranked roles",
     "LoL tip: pick 1–2 roles and a small champion pool to climb efficiently. Riot has confirmed they won't chase collab skins to keep the game's tone intact."),
    ("valorant tactical shooter riot agents abilities",
     "Valorant rewards strong aim + utility usage. Master a few agents before expanding your pool. Still one of the most popular tactical shooters in 2026."),

    # --- VR / RETRO / OTHER ---
    ("vr virtual reality headset meta quest games",
     "Meta Quest 3 is still the top standalone VR headset in 2026. Try Beat Saber, Superhot VR, and Half-Life Alyx for PCVR."),
    ("retro classic old games emulator nostalgia",
     "Retro gaming: emulators, GOG classics, or Nintendo Switch 2 Online for legal retro libraries. Oblivion Remastered (2025) is a great way to revisit a classic."),
    ("game lore story universe deep worldbuilding",
     "Deep lore games: Elden Ring (and Nightreign), Destiny 2, Mass Effect Legendary Edition, Dark Souls series, and Clair Obscur: Expedition 33."),

    # --- BEGINNER ---
    ("beginner new gamer start easy games",
     "Start with Minecraft, Stardew Valley, Portal 2, or Terraria — beginner-friendly and genuinely fun. Split Fiction is also great if you have a friend to play with."),
]

question_texts = [q for q, a in qa_pairs]
question_embedding = model.encode(question_texts, convert_to_tensor=True)

THRESHOLD = 0.3

def get_response(user_input):
    input_embedding = model.encode(user_input, convert_to_tensor=True)
    similarities = util.cos_sim(input_embedding, question_embedding)[0]
    best_idx = similarities.argmax().item()
    best_score = similarities[best_idx].item()

    if best_score < THRESHOLD:
        return best_score, "Sorry, I don't understand. Try asking about games, hardware, or gaming tips!"

    return best_score, qa_pairs[best_idx][1]

class ChatbotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gaming Chatbot")
        self.root.geometry("500x600")
        self.root.configure(bg="#2E2E2E")

        # Title
        tk.Label(
            root, text="Gaming Chatbot", font=("Helvetica", 16, "bold"),
            fg="#FFFFFF", bg="#2E2E2E"
        ).pack(pady=10)

        # Chat area (scrollable)
        self.chat_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, height=20, width=50, font=("Arial", 11),
            bg="#3C3C3C", fg="#E0E0E0", insertbackground="white"
        )
        self.chat_area.pack(pady=10, padx=10)
        self.chat_area.insert(tk.END,
                              "🎮 Welcome to the Gaming Chatbot!\n\n"
                              "Not sure what to ask? Here are some ideas:\n"
                              "  • 'What are the best new games in 2026?'\n"
                              "  • 'My FPS is dropping — how do I fix it?'\n"
                              "  • 'Best GPU for 1440p gaming right now?'\n"
                              "  • 'I'm new to gaming, where do I start?'\n\n"
                              "Go ahead and ask anything!\n")
        self.chat_area.config(state='disabled')

        input_frame = tk.Frame(self.root, bg="#2E2E2E")
        input_frame.pack(pady=5)

        self.input_field = tk.Entry(
            input_frame, width=40, font=("Arial", 12, "bold"), bg="#4A4A4A", fg="#FFFFFF",
            insertbackground="white"
        )
        self.input_field.pack(side=tk.LEFT, padx=5)
        self.input_field.bind("<Return>", self.send_message)

        tk.Button(
            input_frame, text="Send", command=self.send_message, font=("Arial", 12),
            bg="#4CAF50", fg="#FFFFFF", activebackground="#45A094"
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            root, text="Clear Chat", command=self.clear_chat, font=("Arial", 12),
            bg="#F44336", fg="#FFFFFF", activebackground="#D32F2F"
        ).pack(pady=5)

    def send_message(self, event=None):
        user_input = self.input_field.get()
        if not user_input:
            return

        score, response = get_response(user_input)
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"\nYou: {user_input}\n")
        self.chat_area.insert(tk.END, f"Match confidence: {score:.2f}\n")
        self.chat_area.insert(tk.END, f"Bot: {response}\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)
        self.input_field.delete(0, tk.END)

    def clear_chat(self):
        self.chat_area.config(state='normal')
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.insert(tk.END, "🎮 Chat cleared. Ask me anything about games, hardware, or fixes!\n")
        self.chat_area.config(state='disabled')


def main():
    root = tk.Tk()
    app = ChatbotUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()