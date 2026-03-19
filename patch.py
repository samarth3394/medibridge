import os
import sys

base_dir = r"c:\Users\User\.gemini\antigravity\playground\binary-blazar\medical_sys"

# 1. Fix HTML templates variables for missing buttons
templates_dir = os.path.join(base_dir, "templates")
for root, _, files in os.walk(templates_dir):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            # Fix button colors
            content = content.replace('var(--primary-color)', 'var(--primary-blue)')
            content = content.replace('var(--success)', 'var(--soft-green)')
            content = content.replace('var(--error)', '#ef4444')
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

# 2. Fix Database User
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medical_sys.settings")
import django
django.setup()
from accounts.models import CustomUser

try:
    u = CustomUser.objects.get(username='admin')
    u.username = 'sammy3394'
    u.set_password('sammy@3394')
    u.save()
    print("User updated to sammy3394!")
except CustomUser.DoesNotExist:
    pass

try:
    u = CustomUser.objects.get(username='sammy3394')
    u.set_password('sammy@3394')
    u.save()
    print("User sammy3394 password guaranteed.")
except CustomUser.DoesNotExist:
    pass
