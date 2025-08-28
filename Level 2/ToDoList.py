import csv

def add(task, file):
    csvfile = file+'.csv'
    mod = []
    count = 0
    with open(csvfile, "r", newline='') as test:
        existing_info = csv.reader(test)
        for row in existing_info:
            count += 1
            mod.append(row)
        mod.append(task)
        
    with open(csvfile, "w", newline="") as doc:
        info = csv.writer(doc)
        info.writerows(mod)
    
    return print('List Updated\n')

def remove(num, file):
    csvfile = file+'.csv'
    print(csvfile)
    mod =[]
    count = 0
    number = 1
    num = str(num)

    with open(csvfile, "r", newline='') as test:
        existing_info = csv.reader(test)
        for row in existing_info:
            count += 1
    
    if count>1:

        with open(csvfile, "r", newline="") as doc:
            info = list(csv.reader(doc))
            for row in info:
                if row[0] == 'Number':
                    mod.append(row)
                    #print(mod)

                elif row[0] != num:
                    task = row[1]
                    status = row[2]
                    row = [number, task, status]
                    mod.append(row)
                    number += 1
                
                else:
                    pass
                
                #print(mod)

        with open(csvfile, "w", newline="") as newdoc:
            new_info = csv.writer(newdoc)
            new_info.writerows(mod)
        
        return print('List Updated\n')
    
    else:

        return print('There are no tasks')

def done(num, file):
    csvfile = file+'.csv'
    mod = []
    count = 0
    num = str(num)

    with open(csvfile, "r", newline='') as test:
        existing_info = csv.reader(test)
        for row in existing_info:
            count += 1
    
    if count>1:

        with open(csvfile, 'r', newline='') as oldfile:
            info = csv.reader(oldfile)
            for row in info:
                if row[0] == 'Number':
                    mod.append(row)
                    #print(mod)

                elif row[0] == num:
                    row[2] = 'Done'
                    mod.append(row)
                    #print(mod)
                
                elif row[0] != num:
                    mod.append(row)
                    #print(mod)
                
                else:
                    pass
        
        with open (csvfile, 'w', newline='') as newfile:
            new_info = csv.writer(newfile)
            new_info.writerows(mod)
        
        return print('List Updated\n')
    
    else:

        return print('There are no tasks')

def undone(num, file):
    csvfile = file+'.csv'
    mod = []
    count = 0
    num = str(num)
    with open(csvfile, "r", newline='') as test:
        existing_info = csv.reader(test)
        for row in existing_info:
            count += 1
    
    if count>1:

        with open(csvfile, 'r', newline='') as oldfile:
            info = csv.reader(oldfile)
            for row in info:
                if row[0] == 'Number':
                    mod.append(row)
                    #print(mod)

                elif row[0] == num:
                    row[2] = 'Undone'
                    mod.append(row)
                    #print(mod)
                
                elif row[0] != num:
                    mod.append(row)
                    #print(mod)
                
                else:
                    pass
        
        with open (csvfile, 'w', newline='') as newfile:
            new_info = csv.writer(newfile)
            new_info.writerows(mod)
        
        return print('List Updated\n')
    
    else:

        return print('There are no tasks')

while True:

    user_input = input('\nWelcome to My To Do List\n\n1. Open existing file\n2. Create new file\n3. Exit\n-> ')

#---------------------------------------------------------------------------------------------------
#Option 1 with existing file open
#---------------------------------------------------------------------------------------------------

    if user_input == '1':
        filename = input('\nEnter filename\n-> ')
        csvfile = filename+'.csv'
        count = -1
        check = True
        try:
            with open(csvfile, "r", newline="") as existingfile:
                read = csv.reader(existingfile)
                for row in read:
                    #print(row)
                    count +=1
        except FileNotFoundError:
            print('\n!!File does not exist!!\n!!Please try again!!\n')
            check = False
            

        while check == True:
            with open(csvfile, "r", newline="") as existingfile:
                read = csv.reader(existingfile)
                for row in read:
                    print(row)
                    #count +=1

            second_choice = input('\nDo you want to\n1. Add new task \n2. Delete existing task \n3. Mark Task as Done \n4. Mark Task as Undone \n5. Exit\n-> ')

            if second_choice == '1':
                data = []
                new_task = str(input('Add new task\n-> '))
                count += 1
                data = [count, new_task, 'Undone']
                add(data, filename)
            
            elif second_choice == '2':
                while True:   
                    
                    if count >=1:
                        third_choice = int(input('Select the number associated with the task you want to delete\n-> '))
                        try:
                            if third_choice <=0:
                                print('Choose a number associated with the task you want to delete\n')
                            
                            elif third_choice > count:
                                print('Choose a number associated with the task you want to delete\n')
                            
                            else:
                                remove(third_choice, filename)
                                break

                        except ValueError:
                            print('Enter a integer value\n')
                    
                    else:
                        print('\nNo tasks yet. Please add new task\n')
                        break
            
            elif second_choice == '3':
                while True:

                    if count >=1:
                        third_choice = int(input('Select the number associated with the task you want to mark as DONE\n-> '))
                        try:
                            if third_choice <=0:
                                print('Choose a number associated with the task you want to mark as DONE\n')
                            
                            elif third_choice > count:
                                print('Choose a number associated with the task you want to mark as DONE\n')
                            
                            else:
                                done(third_choice, filename)
                                break

                        except ValueError:
                            print('Enter a integer value\n')
                        
                    else:
                        print('\nNo tasks yet. Please add new task\n')
                        break
            
            elif second_choice == '4':
                while True:

                    if count >=1:

                        third_choice = int(input('Select the number associated with the task you want to mark as UNDONE\n-> '))
                        try:
                            if third_choice <=0:
                                print('Choose a number associated with the task you want to mark as UNDONE\n')
                            
                            elif third_choice > count:
                                print('Choose a number associated with the task you want to mark as UNDONE\n')
                            
                            else:
                                undone(third_choice, filename)
                                break

                        except ValueError:
                            print('Enter a integer value\n')

                    else:
                        print('\nNo tasks yet. Please add new task\n')
                        break
            
            elif second_choice == '5':
                break

            else:
                print('\nInvalid choice\n')

#---------------------------------------------------------------------------------------------------
#Option 2 with new file open
#---------------------------------------------------------------------------------------------------

    elif user_input == '2':
        filename = input('\nEnter new filename\n-> ')
        csvfile = filename+'.csv'
        data = ["Number", "Task", "Done/Undone"]
        try:
            with open(csvfile, "r", newline="") as oldfile:
                read = csv.reader(oldfile)
                print('\nFile exists')

        except FileNotFoundError:
            print(f'\nFile {filename} has been created\n')
        
        finally:
            with open(csvfile, 'w', newline='') as newfile:
                write = csv.writer(newfile)
                write.writerow(data)
                count = 0

        while True:
            second_choice = input('\nDo you want to\n1. Add new task \n2. Delete existing task \n3. Mark Task as Done \n4. Mark Task as Undone \n5. Exit \n-> ')

            if second_choice == '1':
                data = []
                new_task = str(input('Add new task\n-> '))
                count+=1
                data = [count, new_task, 'Undone']
                add(data, filename)
                break
            
            elif second_choice == '2':
                while True:
                    third_choice = 0
                    
                    remove(third_choice, filename)
                    break

            
            elif second_choice == '3':
                while True:
                    third_choice = 0
                    
                    done(third_choice, filename)
                    break  
            
            elif second_choice == '4':
                while True:
                    third_choice = 0
                    
                    undone(third_choice, filename)
                    break    

            elif second_choice == '5':
                break

            else:
                print('Invalid choice')     

#---------------------------------------------------------------------------------------------------
#Option 3 with new file open
#---------------------------------------------------------------------------------------------------

    elif user_input == '3':
        print('\nThank You')
        break

#---------------------------------------------------------------------------------------------------
#Option 4 with new file open
#---------------------------------------------------------------------------------------------------

    else:
        print('\nPick Valid Option\n')
