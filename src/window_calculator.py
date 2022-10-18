total_month = 12
class WindowCalculator:
  """
  module for calculate window and other realted algoritmic implementations
  """
  
  
  no_of_periods = 1   #possible values: 1, 2, 4, 12
  current_month = 1   #possible values: 1 to 12
  
   

  def __init__(self):
    print("initializing window calculator class...")
    
  @staticmethod  
  def get_window_id(no_of_periods, current_month):
    """
    takes two integers no_of_periods & current_month and returns the relevant window_id
    """
    window = -1         #possible values: 0 to 11, default = -1
    step = int(total_month/no_of_periods) # calculate the step raiser
    month_upper_range = range(0, total_month, step)
    for mont_upper in month_upper_range:
      if mont_upper >= current_month:
        break
      else:
        window = window + 1
    return window
    
  @staticmethod
  def print_windows_ids():
    print("no_of_periods"+ "\t" + "current_month" + "\t" + "window")
    for no_of_periods in [1,2,4,12]:
      for current_month in range(1, total_month+1):
        print(str(no_of_periods) + "\t \t" + str(current_month) + "\t \t" + str(WindowCalculator.get_window_id(no_of_periods, current_month)))
      
      
