public Map<String, Integer> word0(String[] strings) {
  Map<String, Integer> mp = new HashMap();
  for (int i = 0; i < strings.length; i++)
    mp.put(strings[i],0);
  return mp;
}
