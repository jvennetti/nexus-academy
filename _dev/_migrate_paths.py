#!/usr/bin/env python3
"""
Update all HTML/JS path references after file reorganization.

Depth conventions:
  depth=0  -> root HTML files (hub-*.html, 404.html)
  depth=1  -> files in module-N/, pre-course/, machine/, bonus/
"""
import os, re, glob

BASE = '/home/user/nexus-academy'

# ── Audio mapping: old_name -> new_path_from_root ──────────────────────────
AUDIO = {
    'ciro-intro song.mp3':                          'audio/music/ciro-intro.mp3',
    'hub_music.mp3':                                'audio/music/hub-theme-v1.mp3',
    'hub_music_2.mp3':                              'audio/music/hub-theme.mp3',
    'machine_input_page_music.wav':                 'audio/music/machine-ambient.wav',
    'machine_unlock_music.mp3':                     'audio/music/machine-unlock.mp3',
    'module_complete_music.mp3':                    'audio/music/module-complete.mp3',
    'decrypting_noise_17_seconds.wav':              'audio/sfx/decrypting-noise.wav',
    'password_confirmation.mp3':                    'audio/sfx/password-confirm.mp3',
    'power_on_1.mp3':                               'audio/sfx/power-on-1.mp3',
    'power_on_2.mp3':                               'audio/sfx/power-on-2.mp3',
    'power_on_3.mp3':                               'audio/sfx/power-on-3.mp3',
    'robot_error_1_second.wav':                     'audio/sfx/robot-error.wav',
    'robot_error_1_second_play3times_for_error.wav':'audio/sfx/robot-error-x3.wav',
    'robot_failure_5_seconds.mp3':                  'audio/sfx/robot-failure.mp3',
    'short_success_1_second.wav':                   'audio/sfx/short-success.wav',
    'transition_sound_effect.wav':                  'audio/sfx/transition-1.wav',
    'transition_sound_effect_2.wav':                'audio/sfx/transition-2.wav',
    'transition_sound_effect_3.wav':                'audio/sfx/transition-3.wav',
    'wait_sound_3_seconds.wav':                     'audio/sfx/wait-sound.wav',
}

# ── Image mapping: old_name -> new_path_from_root ─────────────────────────
IMAGES = {
    'Bonus_Vault_art.png':              'images/bonus-vault.png',
    'Challenge Image_ Module 1.png':   'images/modules/m1-challenge.png',
    'Challenge Image_ Module 2.png':   'images/modules/m2-challenge.png',
    'Challenge Image_ Module 3.png':   'images/modules/m3-challenge.png',
    'Challenge Image_ Module 4.png':   'images/modules/m4-challenge.png',
    'Challenge Image_ Module 5.png':   'images/modules/m5-challenge.png',
    'Challenge Image_ Module 6.png':   'images/modules/m6-challenge.png',
    'Module_1_Locked.png':             'images/modules/m1-locked.png',
    'Module_1_Unlocked.png':           'images/modules/m1-unlocked.png',
    'Module_2_Locked.png':             'images/modules/m2-locked.png',
    'Module_2_Unlocked.png':           'images/modules/m2-unlocked.png',
    'Module_3_Locked.png':             'images/modules/m3-locked.png',
    'Module_3_Unlocked.png':           'images/modules/m3-unlocked.png',
    'Module_4_Locked.png':             'images/modules/m4-locked.png',
    'Module_4_Unlocked.png':           'images/modules/m4-unlocked.png',
    'Module_5_Locked.png':             'images/modules/m5-locked.png',
    'Module_5_Unlocked.png':           'images/modules/m5-unlocked.png',
    'Module_6_Locked.png':             'images/modules/m6-locked.png',
    'Module_6_Unlocked.png':           'images/modules/m6-unlocked.png',
    'Module_7_Locked.png':             'images/modules/m7-locked.png',
    'Module_7_Unlocked.png':           'images/modules/m7-unlocked.png',
    'og-preview.png':                  'images/og-preview.png',
}

# ── HTML page link mapping: old_path -> new_path (as seen from root) ──────
PAGE_LINKS = {
    'machine-input.html':    'machine/input.html',
    'machine-activated.html':'machine/activated.html',
    'bonus-vault.html':      'bonus/vault.html',
}

def file_depth(filepath):
    """How many directory levels below BASE is this file?"""
    rel = os.path.relpath(filepath, BASE)
    parts = rel.split(os.sep)
    return len(parts) - 1  # -1 because last part is the filename

def prefix(depth):
    return '../' * depth

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    original = content
    depth = file_depth(filepath)
    pre = prefix(depth)  # '' for root, '../' for depth-1, etc.

    # ── Audio replacements ──────────────────────────────────────────────────
    for old, new in AUDIO.items():
        old_escaped = re.escape(old)
        # Match with optional leading ../ prefix (any number of levels)
        # Replace: (optional_prefix)(old_name) -> (pre)(new)
        # We match what's currently there and replace with the correct prefix
        content = re.sub(
            r'(\.\./)*' + old_escaped,
            pre + new,
            content
        )

    # ── Image replacements ──────────────────────────────────────────────────
    for old, new in IMAGES.items():
        old_escaped = re.escape(old)
        content = re.sub(
            r'(\.\./)*' + old_escaped,
            pre + new,
            content
        )

    # ── Absolute OG image URL (only in hub pages) ──────────────────────────
    content = content.replace(
        'https://jvennetti.github.io/nexus-academy/og-preview.png',
        'https://jvennetti.github.io/nexus-academy/images/og-preview.png'
    )

    # ── Page link replacements ──────────────────────────────────────────────
    for old, new in PAGE_LINKS.items():
        old_escaped = re.escape(old)
        # Handle both bare name (from root) and with ../ prefix (from subdirs)
        # and even relative paths like href="machine-input.html" or href="../machine-input.html"
        content = re.sub(
            r'(\.\./)*' + old_escaped,
            pre + new,
            content
        )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {os.path.relpath(filepath, BASE)}')
    else:
        print(f'No change: {os.path.relpath(filepath, BASE)}')

def main():
    html_files = []
    for root, dirs, files in os.walk(BASE):
        # Skip .git and _dev
        dirs[:] = [d for d in dirs if d not in ('.git', '_dev', 'audio', 'images', 'js')]
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))

    print(f'Processing {len(html_files)} HTML files...\n')
    for fp in sorted(html_files):
        process_file(fp)

    # ── Update nexus-transition.js (stays at root, uses currentScript-relative paths) ──
    js_path = os.path.join(BASE, 'nexus-transition.js')
    with open(js_path, 'r') as f:
        js = f.read()
    orig_js = js
    js = js.replace("'transition_sound_effect.wav'", "'audio/sfx/transition-1.wav'")
    js = js.replace("'transition_sound_effect_2.wav'", "'audio/sfx/transition-2.wav'")
    js = js.replace("'transition_sound_effect_3.wav'", "'audio/sfx/transition-3.wav'")
    if js != orig_js:
        with open(js_path, 'w') as f:
            f.write(js)
        print('\nUpdated: nexus-transition.js')

if __name__ == '__main__':
    main()
