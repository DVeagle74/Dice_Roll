import tkinter as Tk
import random



def clicked_add(val):
    val.set(val.get() + 1)
    calc_num_total()
def clicked_subtract(val):
    if val.get() > 0:
        val.set(val.get() - 1)
    calc_num_total()
    
def clicked_subtract_mod(val):
    val.set(val.get() - 1)
        
def calc_num_total():
    total_num_dice.set(counter_d4.get() + counter_d6.get() + counter_d8.get())

def clicked_roll():
    #d4
    roll_dice(counter_d4.get(), 4, display_str_d4, total_d4, modify_d4)
    #d6
    roll_dice(counter_d6.get(), 6, display_str_d6, total_d6, modify_d6)
    #d8
    roll_dice(counter_d8.get(), 8, display_str_d8, total_d8, modify_d8)
    
def roll_dice(num_dice, dice_type, out_string, total_var, mod_var):
    dice_vals = []

    for i in range(num_dice):
        curr_val = random.randint(1, dice_type)
        dice_vals.append(curr_val)

    total_var.set(sum(dice_vals) + mod_var.get())    
    res_list = ' + '.join(map(str, dice_vals))
    out_string.set(res_list + ' + ' + str(mod_var.get()) + ' = ' + str(sum(dice_vals) + mod_var.get()))
    calc_roll_total()
    
def calc_roll_total():
    total_roll.set(total_d4.get() + total_d6.get() + total_d8.get())        



root = Tk.Tk()
root.title("Counter")
root.geometry("")

total_num_dice = Tk.IntVar()
total_num_dice.set(0)
total_roll = Tk.IntVar()
total_roll.set(0)


counter_d4 = Tk.IntVar()
counter_d4.set(0)
modify_d4 = Tk.IntVar()
modify_d4.set(0)
total_d4 = Tk.IntVar()
total_d4.set(0)

display_str_d4 = Tk.StringVar()
display_str_d4.set("")

b_plus_d4 = Tk.Button(root, text = "+", command = lambda: clicked_add(counter_d4))
b_plus_d4.grid(row = 0, column = 3)
b_minus_d4 = Tk.Button(root, text = "-", command = lambda: clicked_subtract(counter_d4))
b_minus_d4.grid(row = 0, column = 1)

b_plus_mod_d4 = Tk.Button(root, text = "+", command = lambda: clicked_add(modify_d4))
b_plus_mod_d4.grid(row = 0, column = 6)
b_minus_mod_d4 = Tk.Button(root, text = "-", command = lambda: clicked_subtract_mod(modify_d4))
b_minus_mod_d4.grid(row = 0, column = 4)

L_d4_name = Tk.Label(root, text = "D4")
L_d4_name.grid(row = 0, column = 0)
L_d4_count = Tk.Label(root, textvariable = counter_d4)
L_d4_count.grid(row = 0, column = 2)
L_d4_mod = Tk.Label(root, textvariable = modify_d4)
L_d4_mod.grid(row = 0, column = 5)
L_d4_total = Tk.Label(root, textvariable = display_str_d4)
L_d4_total.grid(row = 0, column = 7)


counter_d6 = Tk.IntVar()
counter_d6.set(0)
modify_d6 = Tk.IntVar()
modify_d6.set(0)
total_d6 = Tk.IntVar()
total_d6.set(0)

display_str_d6 = Tk.StringVar()
display_str_d6.set("")

b_plus_d6 = Tk.Button(root, text = "+", command = lambda: clicked_add(counter_d6))
b_plus_d6.grid(row = 1, column = 3)
b_minus_d6 = Tk.Button(root, text = "-", command = lambda: clicked_subtract(counter_d6))
b_minus_d6.grid(row = 1, column = 1)

b_plus_mod_d6 = Tk.Button(root, text = "+", command = lambda: clicked_add(modify_d6))
b_plus_mod_d6.grid(row = 1, column = 6)
b_minus_mod_d6 = Tk.Button(root, text = "-", command = lambda: clicked_subtract_mod(modify_d6))
b_minus_mod_d6.grid(row = 1, column = 4)

L_d6_name = Tk.Label(root, text = "D6")
L_d6_name.grid(row = 1, column = 0)
L_d6_count = Tk.Label(root, textvariable = counter_d6)
L_d6_count.grid(row = 1, column = 2)
L_d6_mod = Tk.Label(root, textvariable = modify_d6)
L_d6_mod.grid(row = 1, column = 5)
L_d6_total = Tk.Label(root, textvariable = display_str_d6)
L_d6_total.grid(row = 1, column = 7)

counter_d8 = Tk.IntVar()
counter_d8.set(0)
modify_d8 = Tk.IntVar()
modify_d8.set(0)
total_d8 = Tk.IntVar()
total_d8.set(0)

display_str_d8 = Tk.StringVar()
display_str_d8.set("")

b_plus_d8 = Tk.Button(root, text = "+", command = lambda: clicked_add(counter_d8))
b_plus_d8.grid(row = 2, column = 3)
b_minus_d8 = Tk.Button(root, text = "-", command = lambda: clicked_subtract(counter_d8))
b_minus_d8.grid(row = 2, column = 1)

b_plus_mod_d8 = Tk.Button(root, text = "+", command = lambda: clicked_add(modify_d8))
b_plus_mod_d8.grid(row = 2, column = 6)
b_minus_mod_d8 = Tk.Button(root, text = "-", command = lambda: clicked_subtract_mod(modify_d8))
b_minus_mod_d8.grid(row = 2, column = 4)

L_d8_name = Tk.Label(root, text = "D8")
L_d8_name.grid(row = 2, column = 0)
L_d8_count = Tk.Label(root, textvariable = counter_d8)
L_d8_count.grid(row = 2, column = 2)
L_d8_mod = Tk.Label(root, textvariable = modify_d8)
L_d8_mod.grid(row = 2, column = 5)
L_d8_total = Tk.Label(root, textvariable = display_str_d8)
L_d8_total.grid(row = 2, column = 7)


b_roll = Tk.Button(root, text = "Roll!", command = clicked_roll)
b_roll.grid(row = 3, column = 0)

L_num_dice = Tk.Label(root, text = "Number of Dice: ")
L_num_dice.grid(row = 3, column = 1)
L_total_num_dice = Tk.Label(root, textvariable = total_num_dice)
L_total_num_dice.grid(row = 3, column = 2)

L_roll_total_text = Tk.Label(root, text = "Total: ")
L_roll_total_text.grid(row = 3, column = 3)
L_total_roll = Tk.Label(root, textvariable = total_roll)
L_total_roll.grid(row = 3, column = 4)

root.mainloop()
