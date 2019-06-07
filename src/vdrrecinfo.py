import os

def contains_vdr_info(path):
  if not os.path.isfile(path) and not os.path.isfile(path + '/info'):
    return False
  return True


class VdrRecInfo():
  __channel = ''
  __channel_name = ''
  __title = ''
  __subheading = ''
  __description = ''

  channel: str = ''
  channel_name: str = ''
  title: str = ''
  subheading: str = ''
  description: str = ''
  
  def __init__(self, path):
    """
    Creates new VdrRecInfo

    :param path: Path of recording-directory or info-file
    """
    assert contains_vdr_info(path)
  
    if not os.path.isfile(path):
      path += '/info'
    
    info_file = open(path)
    for line in info_file:
      self.__parse_line(line.strip())
    info_file.close()
  
  
  def __parse_line(self, line):
    """
    Parses a line of vdr-info-file

    :param line: Line of vdr-info-file
    """
    if line.startswith('C '):
      self.__channel = line[2:]
      self.__channel_name = line[2:]
      channel_split = self.__channel.split(' ', 1)
      if len(channel_split) > 1:
        self.__channel_name = channel_split[1]
    elif line.startswith('T '):
      self.__title = line[2:]
    elif line.startswith('S '):
      self.__subheading = line[2:]
    elif line.startswith('D '):
      self.__description = line[2:]
  
  
  def get_channel(self):
    """
    returns channel

    :return: channel
    """
    return self.__channel

  channel = property(get_channel)


  def get_channel_name(self):
    """
    returns only the name of the channel

    :return: channel-name
    """
    return self.__channel_name

  channel_name = property(get_channel_name)

  
  def get_title(self):
    """
    returns title

    :return: title
    """
    return self.__title

  title = property(get_title)

  
  def get_subheading(self):
    """
    returns subheading

    :return: subheading
    """
    return self.__subheading

  subheading = property(get_subheading)

  
  def get_description(self):
    """
    return description

    :return: description
    """
    return self.__description

  description = property(get_description)

