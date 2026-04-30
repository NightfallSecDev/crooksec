import glob, re

# The new unified footer to inject into every page
NEW_FOOTER = '''    <!-- Footer -->
    <footer class="border-t border-white/10 bg-black pt-16 pb-8 px-6">
        <div class="max-w-7xl mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-10 mb-12">

            <!-- Brand -->
            <div class="sm:col-span-2">
                <a href="index.html" class="flex items-center gap-2 mb-4">
                    <i class="fa-solid fa-shield-halved text-brand-cyan text-xl"></i>
                    <span class="text-xl font-bold tracking-tighter text-white font-mono">CROOKSEC</span>
                </a>
                <p class="text-slate-500 text-sm max-w-xs font-light leading-relaxed mb-6">
                    The next evolution in cybersecurity. Human + AI powered to eliminate threats before they materialize.
                </p>
                <div class="flex gap-4">
                    <a href="#" class="w-9 h-9 flex items-center justify-center rounded border border-white/10 text-slate-500 hover:text-brand-cyan hover:border-brand-cyan/40 transition-all text-sm"><i class="fa-brands fa-github"></i></a>
                    <a href="#" class="w-9 h-9 flex items-center justify-center rounded border border-white/10 text-slate-500 hover:text-brand-cyan hover:border-brand-cyan/40 transition-all text-sm"><i class="fa-brands fa-x-twitter"></i></a>
                    <a href="#" class="w-9 h-9 flex items-center justify-center rounded border border-white/10 text-slate-500 hover:text-brand-cyan hover:border-brand-cyan/40 transition-all text-sm"><i class="fa-brands fa-linkedin-in"></i></a>
                    <a href="#" class="w-9 h-9 flex items-center justify-center rounded border border-white/10 text-slate-500 hover:text-brand-cyan hover:border-brand-cyan/40 transition-all text-sm"><i class="fa-brands fa-telegram"></i></a>
                </div>
            </div>

            <!-- Services -->
            <div>
                <h5 class="text-white font-mono text-xs uppercase tracking-widest mb-5 pb-2 border-b border-white/10">Services</h5>
                <ul class="space-y-3 text-slate-500 text-sm">
                    <li><a href="service.html" class="hover:text-brand-cyan transition-colors">Penetration Testing</a></li>
                    <li><a href="service.html" class="hover:text-brand-cyan transition-colors">Red Team Operations</a></li>
                    <li><a href="service.html" class="hover:text-brand-cyan transition-colors">Cloud Security</a></li>
                    <li><a href="service.html" class="hover:text-brand-cyan transition-colors">OSINT &amp; Threat Intel</a></li>
                    <li><a href="service.html" class="hover:text-brand-cyan transition-colors">Managed SOC</a></li>
                    <li><a href="Pricing.html" class="hover:text-brand-cyan transition-colors">View All Plans</a></li>
                </ul>
            </div>

            <!-- Company -->
            <div>
                <h5 class="text-white font-mono text-xs uppercase tracking-widest mb-5 pb-2 border-b border-white/10">Company</h5>
                <ul class="space-y-3 text-slate-500 text-sm">
                    <li><a href="aboutus.html" class="hover:text-brand-cyan transition-colors">About Us</a></li>
                    <li><a href="Case Studies.html" class="hover:text-brand-cyan transition-colors">Case Studies</a></li>
                    <li><a href="patner.html" class="hover:text-brand-cyan transition-colors">Partner Network</a></li>
                    <li><a href="contact.html" class="hover:text-brand-cyan transition-colors">Contact Us</a></li>
                    <li><a href="weareinattck.html" class="text-red-500 hover:text-red-400 transition-colors flex items-center gap-1"><i class="fa-solid fa-radiation text-xs"></i> Active Breach</a></li>
                </ul>
            </div>

            <!-- Legal -->
            <div>
                <h5 class="text-white font-mono text-xs uppercase tracking-widest mb-5 pb-2 border-b border-white/10">Legal</h5>
                <ul class="space-y-3 text-slate-500 text-sm">
                    <li><a href="privacy-policy.html" class="hover:text-brand-cyan transition-colors">Privacy Policy</a></li>
                    <li><a href="terms.html" class="hover:text-brand-cyan transition-colors">Terms &amp; Conditions</a></li>
                    <li><a href="cookie-policy.html" class="hover:text-brand-cyan transition-colors">Cookie Policy</a></li>
                </ul>

                <!-- Emergency CTA -->
                <div class="mt-8 p-4 bg-red-500/5 border border-red-500/20 rounded-lg">
                    <p class="text-red-400 font-mono text-xs mb-2 font-bold"><i class="fa-solid fa-triangle-exclamation mr-1"></i> UNDER ATTACK?</p>
                    <a href="weareinattck.html" class="text-xs text-slate-400 hover:text-red-400 transition-colors leading-relaxed">Trigger emergency incident response &rarr;</a>
                </div>
            </div>

        </div>

        <!-- Bottom Bar -->
        <div class="max-w-7xl mx-auto border-t border-white/10 pt-8 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-600 font-mono gap-4">
            <p class="text-center sm:text-left">&copy; 2026 Crooksec Intelligence. All rights reserved. All offensive operations are conducted under signed authorization only.</p>
            <div class="flex gap-4 shrink-0">
                <a href="privacy-policy.html" class="hover:text-slate-400 transition-colors">Privacy</a>
                <span class="text-slate-800">|</span>
                <a href="terms.html" class="hover:text-slate-400 transition-colors">Terms</a>
                <span class="text-slate-800">|</span>
                <a href="cookie-policy.html" class="hover:text-slate-400 transition-colors">Cookies</a>
            </div>
        </div>
    </footer>'''

# Regex to match any existing footer block
FOOTER_REGEX = re.compile(r'    <!-- Footer -->.*?</footer>', re.DOTALL)

files = glob.glob('/home/kali/Documents/crooksec/*.html')
skip = []  # apply to ALL pages

for filepath in files:
    name = filepath.split('/')[-1]
    content = open(filepath).read()

    if FOOTER_REGEX.search(content):
        content = FOOTER_REGEX.sub(NEW_FOOTER, content)
        open(filepath, 'w').write(content)
        print(f'✓ Updated footer in {name}')
    else:
        print(f'  [SKIP] No matching footer block in {name}')
