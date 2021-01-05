public boolean sleepIn(boolean weekday, boolean vacation) {
  if (!weekday || vacation == true) {
    return true;
  }
  return false;
}
