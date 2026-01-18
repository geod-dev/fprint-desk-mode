import re

with open("/etc/pam.d/system-auth") as f:
    lines = f.readlines()

skip_count = {}
regex_patterns = r"^-?auth\s*\[.*?success=(\d+).*?\]\s+(\S+)"
done = False

for i, line in enumerate(lines):
    if line.startswith("#"):
        continue
    match = re.match(regex_patterns, line)
    if match:
        module_name = match.group(2)
        if module_name == "pam_fprintd.so":
            # adjust upper lines
            for key in list(skip_count.keys()):
                line_match = re.match(regex_patterns, lines[key])
                old_success = int(line_match.group(1))
                lines[key] = lines[key].replace(f"success={old_success}", f"success={old_success+1}")
            # insert our line
            lines.insert(i, "auth       [success=1 default=ignore]  pam_exec.so quiet /usr/bin/fprint_desk_mode\n")
            done = True
            break
        # track skip counts
        skip_count[i] = int(match.group(1))

    # decrement skip counts for previous lines
    for key in list(skip_count.keys()):
        if skip_count[key] > 0:
            skip_count[key] -= 1
        else:
            del skip_count[key]

if not done:
    exit(1)

print("".join(lines))
