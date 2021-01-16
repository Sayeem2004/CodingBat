public Map<String, Integer> wordLen(String[] strings) {
  Map<String, Integer> mp = new HashMap();
  for (int i = 0; i < strings.length; i++)
    mp.put(strings[i],strings[i].length());
  return mp;
}
