import re

with open("/etc/pam.d/system-auth") as f:
    lines = f.readlines()

done = False
skip_count = {}
regex_patterns = r"^-?auth\s*\[.*?success=(\d+).*"

for i, line in enumerate(lines):
    if line.startswith("#"):
        continue

    if "fprint_desk_mode" in line:
        lines.pop(i)
        for key in list(skip_count.keys()):
            line_match = re.match(regex_patterns, lines[key])
            old_success = int(line_match.group(1))
            lines[key] = lines[key].replace(f"success={old_success}", f"success={old_success-1}")
        done = True
        break

    match = re.match(regex_patterns, line)
    if match:
        skip_count[i] = int(match.group(1))

    for key in list(skip_count.keys()):
        if skip_count[key] > 0:
            skip_count[key] -= 1
        else:
            del skip_count[key]

if not done:
    exit(1)

print("".join(lines))
