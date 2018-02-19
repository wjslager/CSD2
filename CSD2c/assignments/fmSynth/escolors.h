#ifndef _ESCOLORS_H_
#define _ESCOLORS_H_

namespace etxt {
  std::string reset    = "\033[0m";

  // Styling
  std::string b        = "\033[1m";
  std::string i        = "\033[3m";
  std::string l        = "\033[4m";
  std::string inv      = "\033[7m";

  // Text colors
  std::string black    = "\033[30m";
  std::string red      = "\033[31m";
  std::string green    = "\033[32m";
  std::string blue     = "\033[34m";
  std::string yellow   = "\033[33m";
  std::string magenta  = "\033[35m";
  std::string cyan     = "\033[36m";
  std::string white    = "\033[37m";
}

namespace ebg {
  // Background colors
  std::string black    = "\033[40m";
  std::string red      = "\033[41m";
  std::string green    = "\033[42m";
  std::string blue     = "\033[44m";
  std::string yellow   = "\033[43m";
  std::string magenta  = "\033[45m";
  std::string cyan     = "\033[46m";
  std::string white    = "\033[47m";
}

#endif
