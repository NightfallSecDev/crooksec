import glob, re

BUTTON_MAP = {
    # index.html hero + pricing buttons
    'index.html': [
        # Hero: Deploy Defense → contact.html
        (
            '<button\n                    class="btn-scan px-8 py-4 bg-brand-cyan hover:bg-brand-cyan/90 text-brand-darker font-bold rounded-sm shadow-[0_0_20px_rgba(6,182,212,0.3)] transition-all w-full sm:w-auto flex items-center justify-center gap-3">\n                    Deploy Defense <i class="fa-solid fa-arrow-right"></i>\n                </button>',
            '<a href="contact.html"\n                    class="btn-scan px-8 py-4 bg-brand-cyan hover:bg-brand-cyan/90 text-brand-darker font-bold rounded-sm shadow-[0_0_20px_rgba(6,182,212,0.3)] transition-all w-full sm:w-auto flex items-center justify-center gap-3">\n                    Deploy Defense <i class="fa-solid fa-arrow-right"></i>\n                </a>'
        ),
        # Hero: View Capabilities → service.html
        (
            '<button\n                    class="px-8 py-4 border border-white/20 hover:border-white/50 bg-white/5 font-bold rounded-sm text-white transition-all w-full sm:w-auto flex items-center justify-center gap-3">\n                    <i class="fa-solid fa-terminal"></i> View Capabilities\n                </button>',
            '<a href="service.html"\n                    class="px-8 py-4 border border-white/20 hover:border-white/50 bg-white/5 font-bold rounded-sm text-white transition-all w-full sm:w-auto flex items-center justify-center gap-3">\n                    <i class="fa-solid fa-terminal"></i> View Capabilities\n                </a>'
        ),
        # Pricing: Deploy P1 → Pricing.html
        (
            'class="w-full py-3 bg-white/5 hover:bg-white/10 text-white font-mono text-sm border border-white/10 rounded transition-colors relative z-10 mt-auto">Deploy\n                        P1</button>',
            'class="w-full py-3 bg-white/5 hover:bg-white/10 text-white font-mono text-sm border border-white/10 rounded transition-colors relative z-10 mt-auto" href="contact.html">Deploy P1</a>'
        ),
        # Pricing: Deploy P2 → Pricing.html
        (
            'class="w-full py-3 bg-brand-cyan hover:bg-brand-cyan/90 text-brand-darker font-bold font-mono text-sm rounded transition-colors relative z-10 mt-auto">Deploy\n                        P2</button>',
            'class="w-full py-3 bg-brand-cyan hover:bg-brand-cyan/90 text-brand-darker font-bold font-mono text-sm rounded transition-colors relative z-10 mt-auto" href="contact.html">Deploy P2</a>'
        ),
        # Pricing: Deploy P3 → contact.html
        (
            'class="w-full py-3 bg-white/5 hover:bg-white/10 text-white font-mono text-sm border border-white/10 rounded transition-colors relative z-10 mt-auto">Deploy\n                        P3</button>',
            'class="w-full py-3 bg-white/5 hover:bg-white/10 text-white font-mono text-sm border border-white/10 rounded transition-colors relative z-10 mt-auto" href="contact.html">Deploy P3</a>'
        ),
        # Pricing: Contact Sales (P4) → contact.html
        (
            'class="w-full py-3 bg-white/5 hover:bg-white/10 text-white font-mono text-sm border border-white/10 rounded transition-colors relative z-10 mt-auto">Contact\n                        Sales</button>',
            'class="w-full py-3 bg-white/5 hover:bg-white/10 text-white font-mono text-sm border border-white/10 rounded transition-colors relative z-10 mt-auto" href="contact.html">Contact Sales</a>'
        ),
        # CTA form submit button → contact.html
        (
            '<button type="button"\n                    class="w-full py-4 bg-brand-cyan hover:bg-brand-cyan/90 text-brand-darker font-bold rounded shadow-[0_0_20px_rgba(6,182,212,0.3)] transition-all flex items-center justify-center gap-2">\n                    Request Free Consultation <i class="fa-solid fa-shield-cat"></i>\n                </button>',
            '<a href="contact.html"\n                    class="w-full py-4 bg-brand-cyan hover:bg-brand-cyan/90 text-brand-darker font-bold rounded shadow-[0_0_20px_rgba(6,182,212,0.3)] transition-all flex items-center justify-center gap-2">\n                    Request Free Consultation <i class="fa-solid fa-shield-cat"></i>\n                </a>'
        ),
    ],
}

# --- Global fixes across ALL pages ---
GLOBAL_REPLACEMENTS = [
    # service.html INIT_SCAN button (it's a button not anchor)
    (
        '<button\n                    class="btn-scan hidden sm:inline-flex px-5 py-2.5 bg-brand-cyan/10 hover:bg-brand-cyan/20 text-brand-cyan border border-brand-cyan/30 rounded-sm font-mono text-sm transition-all shadow-[0_0_15px_rgba(6,182,212,0.15)] hover:shadow-[0_0_25px_rgba(6,182,212,0.3)]">\n                    INIT_SCAN <i class="fa-solid fa-terminal ml-2"></i>\n                </button>',
        '<a href="contact.html"\n                    class="btn-scan hidden sm:inline-flex px-5 py-2.5 bg-brand-cyan/10 hover:bg-brand-cyan/20 text-brand-cyan border border-brand-cyan/30 rounded-sm font-mono text-sm transition-all shadow-[0_0_15px_rgba(6,182,212,0.15)] hover:shadow-[0_0_25px_rgba(6,182,212,0.3)]">\n                    INIT_SCAN <i class="fa-solid fa-terminal ml-2"></i>\n                </a>'
    ),
    # /PARTNERS dropdown button - keep as button (not a link)
    # but the Deploy P1/P2/P3 buttons in Pricing.html are anchor tags already
]

files = glob.glob('/home/kali/Documents/crooksec/*.html')

for filepath in files:
    filename = filepath.split('/')[-1]
    with open(filepath, 'r') as f:
        content = f.read()

    # Apply file-specific fixes
    if filename in BUTTON_MAP:
        for old, new in BUTTON_MAP[filename]:
            content = content.replace(old, new)

    # Apply global fixes
    for old, new in GLOBAL_REPLACEMENTS:
        content = content.replace(old, new)

    # Fix pricing button tags: <button class="...">Deploy P1</button> → <a href="contact.html" ...>
    # These are the ones inside Pricing.html
    content = re.sub(
        r'<button\s+class="(text-center w-full py-3 [^"]+)"\s*>\s*(Deploy P[1-3]|Contact Sales)\s*</button>',
        lambda m: f'<a href="contact.html" class="{m.group(1)}" style="display:block">{m.group(2)}</a>',
        content
    )

    with open(filepath, 'w') as f:
        f.write(content)
    print(f'Fixed buttons in {filename}')
