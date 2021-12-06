#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# EMalina, 2021-Dec-05 added code to complete assignment 8
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD():
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods: none
    """
    # TODOne Add Code to the CD class
    # -- Constructor -- #
    
    def __init__(self, idid, title, artist):
        #    -- Attributes -- #
        self.__cd_id = idid
        self.__cd_title = title
        self.__cd_artist = artist

    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, idid):
        if str(idid).isnumeric():
            self.__cd_id = idid
        else:
            raise Exception('Non-numeric ID')
        
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, title):
        if str(title).isnumeric():
            raise Exception('Title cannot be number')
        else:
            self.__cd_title = title
            
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, artist):
        if str(artist).isnumeric():
            raise Exception('artist cannot be number')
        else:
            self.__cd_artist = artist    
            
    
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties: none

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODOne Add code to process data from a file
    @staticmethod
    def load_inventory(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                table.append(dicRow)
            objFile.close()
            return table
        except FileNotFoundError as e:
            print('File not found')
            print('Built in error info: ')
            print(type(e), e, e.__doc__, sep='\n')
            table = []
            return table
    
    # TODOne Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, table):
        """Function to save the CD to file
        Args:
            file_name (str): file name for saving
            table (list): current inventory of CDs.  A list of dictionaries
        
        Returns: none
        """
        try:
            objFile = open(file_name, 'w')
            for row in table:
                lstValues = list(row.values())
                lstValues[0] = str(lstValues[0])
                objFile.write(','.join(lstValues) + '\n')
            objFile.close()
        except FileNotFoundError as e:
            print('File not found')
            print('Built in error info: ')
            print(type(e), e, e.__doc__, sep='\n')          

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODOne add docstring
    """Processes data to and from file:

    properties: none

    methods:
        menu(): -> None (prints menu)
        selection(): -> (menu choice)
        inventory(table): -> None (prints inventory)
        add_data(): -> var1, var2, var3 (cd_ID, cd_Title, cd_Artist)

    """
    # TODOne add code to show menu to user
    def menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
    
    # TODOne add code to captures user's choice
    def selection():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    # TODOne add code to display the current data on screen
    def inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """

        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
    
    # TODOne add code to get CD data from user
    def add_data():
        """requests user to input new CD information
        
        Args: none
            
        Returns: tuple of 3;
        var1 (int): ID number
        var2 (str): CD title
        var3 (str): CD artist
        """
        print('Please enter a new CD ID, Title and Artist')
        var1 = input('Enter ID: ').strip()
        var2 = input('What is the CD\'s title? ').strip()
        var3 = input('What is the Artist\'s name? ').strip()
        return(var1, var2, var3)
    pass


# -- Main Body of Script -- #
# TODOne Add Code to the main body
# Load data from file into a list of CD objects on script start
FileIO.load_inventory(strFileName, lstOfCDObjects)
while True:
    # Display menu to user
    IO.menu()
    strChoice = IO.selection()
    # let user exit program
    if strChoice == 'x':
        break
    # show user current inventory
    if strChoice == 'i':
        IO.inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # let user add data to the inventory
    elif strChoice == 'a':
        strID, strTitle, strArtist = IO.add_data()
        newCD = CD(strID, strTitle, strArtist)
        dicRow = {'ID': '{}'.format(newCD.cd_id), 'Title': '{}'.format(newCD.cd_title), 'Artist': '{}'.format(newCD.cd_artist)}
        lstOfCDObjects.append(dicRow)
        IO.inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # let user save inventory to file
    elif strChoice == 's':
        IO.inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # let user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.inventory(lstOfCDObjects)
        continue  # start loop back at top.
    else:
        print('General Error')
