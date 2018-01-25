def generate_perms(s):
  if len(s) == 0:
    return [""]
  ret = []
  for i in range(len(s)):
    shorter = s[0:i] + s[i+1:]
    short_perms = generate_perms (shorter)
    for p in short_perms:
     
      new_perm = s[i] + p
      if new_perm not in ret:
        ret.append (new_perm)
  return ret
a=raw_input("E:")
print generate_perms(a)
