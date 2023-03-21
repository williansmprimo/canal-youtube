import os

def evaluate(state, case):
  if(state[0] == case and state[1] == case and state[2] == case):
    return 1;
  if(state[3] == case and state[4] == case and state[5] == case):
    return 1;
  if(state[6] == case and state[7] == case and state[8] == case):
    return 1;
  if(state[0] == case and state[3] == case and state[6] == case):
    return 1;
  if(state[1] == case and state[4] == case and state[7] == case):
    return 1;
  if(state[2] == case and state[5] == case and state[8] == case):
    return 1;
  if(state[0] == case and state[4] == case and state[8] == case):
    return 1;
  if(state[6] == case and state[4] == case and state[2] == case):
    return 1;
    
  for i in range(0, len(state)):
    if(state[i] == ' '):
      return 0;
  return 2;

def try_state(state, atual_case, nivel):
  if(evaluate(state, atual_case) == 1):
    if(atual_case == 'o'):
      return 1, -1
    else:
      return -1, -1
  if(evaluate(state, atual_case) == 2):
    return 0, -1;
  best_state = 0;
  vl_best_state = -2;
  vl_actual_state = 0;
  for i in range(0, len(state)):
    if(state[i] == ' '):
      if(atual_case == 'x'):
        state[i] = 'o'
      else:
        state[i] = 'x'
      vl_state, nxt_estate = try_state(state, state[i], nivel + 1);
      vl_actual_state += vl_state
      if(vl_state > vl_best_state):
        vl_best_state = vl_state;
        best_state = i
      state[i] = ' '
  return vl_actual_state / nivel, best_state;
  
def print_state(state):
  os.system("clear");
  print("-------------");
  print('|', state[0], '|', state[1], '|', state[2], '|');
  print("-------------");
  print('|', state[3], '|', state[4], '|', state[5], '|');
  print("-------------");
  print('|', state[6], '|', state[7], '|', state[8], '|');
  print("-------------");

def steps():
  globalState = [' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' '];
  while(True):
    print_state(globalState);
    position =  int(input("x:"));
    globalState[position] = 'x';
    print_state(globalState);
    vl_best, best_position = try_state(globalState, 'x', 1);
    if(best_position == -1 and vl_best == -1):
      print("Você ganhou!!");
      return;
    if(best_position == -1 and vl_best == 0):
      print("Empatou!!");
      return;
    globalState[best_position] = 'o';
    print_state(globalState);
    vl_best, best_position = try_state(globalState, 'o', 1);
    if(best_position == -1 and vl_best == 1):
      print("Você perdeu!!");
      return;
    if(best_position == -1 and vl_best == 0):
      print("Empatou!!");
      return;
    #print_state(globalState);
      
steps();
