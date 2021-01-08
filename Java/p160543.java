public String alarmClock(int day, boolean vacation) {
  if (vacation) return (day < 6 && day > 0) ? "10:00" : "off";
  return (day < 6 && day > 0) ? "7:00" : "10:00";
}
