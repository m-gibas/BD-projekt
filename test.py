import PySimpleGUI as sg

# Gereate the data from all bytes image in PySimpleGUI module
i, width = 0, 0
data = {}
for item in dir(sg):
    attribute = getattr(sg, item)
    if isinstance(attribute, bytes):
        data[f'{i:0>2d}'] = (item, attribute)
        width = max(width, len(item))
        i += 1

sg.set_options(font=('Courier New', 11))

ids     = [key for key in data]
items   = [value[0] for value in data.values()]
height  = len(ids)

listboxes = [
    [sg.Listbox(ids,   size=(    2, height), pad=(0, 0), no_scrollbar=True, enable_events=True, key='IDS'),
     sg.Listbox(ids,   size=(    2, height), pad=(0, 0), no_scrollbar=True, enable_events=True, key='IDS'),
     sg.Listbox(items, size=(width, height), pad=(0, 0), no_scrollbar=True, enable_events=True, key='ITEMS')],
]
layout = [
    [sg.Text('Attribute Filter'),
     sg.Input(enable_events=True, expand_x=True, key='FILTER')],
    [sg.Text('ID'),
     sg.Text('Attribute', justification='center', size=width),
     sg.Text('Show', justification='center', expand_x=True)],
    [sg.Column(listboxes, scrollable=True,  vertical_scroll_only=True, key='COLUMN'),
     sg.Image(background_color='green', size=(56, 56), expand_x=True, expand_y=True, key='IMAGE')],
]
window = sg.Window('Title', layout, finalize=True)
lists = ('IDS', 'ITEMS')
for key in lists:
    window[key].widget.configure(activestyle='none')    # Remove underline in Listbox

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    print(event)
    if event in lists:
        selects = window[event].get_indexes()           # Get the indexes for the selection
        if not selects:
            continue
        for key in lists:
            window[key].update(set_to_index=selects)    # Set same selection for all listbox if clicked
        key = window['IDS'].get()[0]                    # Show image for the selected item
        if key in data:
            image = data[key][1]
            window['IMAGE'].update(data=image)
    elif event == 'FILTER':
        text = values['FILTER']
        new_ids, new_items = [], []                     # Create two lists for two listbox if filter
        if text:
            for key, value in data.items():
                if text.lower() in value[0].lower():
                    new_ids.append(key)
                    new_items.append(value[0])
            window['IDS'].update(new_ids)
            window['ITEMS'].update(new_items)
            height = max(len(new_ids), (len(ids)+1)//2) # Keep the minimum height same as the Column element
        else:
            window['IDS'].update(ids)
            window['ITEMS'].update(items)
            height = len(ids)

        window['IDS'].widget.configure(height=height)   # Set the height of Listbox, tkinter code required here
        window['ITEMS'].widget.configure(height=height)
        window.refresh()                                # Update the scroll region of Column element
        window['COLUMN'].contents_changed()

window.close()