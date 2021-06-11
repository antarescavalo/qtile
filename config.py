import os
import subprocess

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

### RUNNING STARTUP SCRIPT ###
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

#### SET VARIABLES ###
mod = "mod4"
terminal = "urxvt"
rofi = "rofi -show run"

### KEYBINDS ###
keys = [

    ### MOST USED BINDS ###
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "f", lazy.spawn('firefox'), desc="Launch browser"),
    Key([mod], "d", lazy.spawn(rofi), desc="Launch rofi"),
    Key([mod], "n", lazy.spawn('nemo'), desc="Launch file manager"),
    Key([mod], "x", lazy.spawn('evince'), desc="Launch xpdf reader"),
    Key([mod], "e", lazy.spawn('evernote-client'), desc="Launch Evernote"),
    Key([mod], "t", lazy.spawn('thunderbird'), desc="Launch thunderbird"),
    Key([mod], "c", lazy.spawn('code'), desc="Launch VSCode"),
    Key([mod], "z", lazy.spawn('keepass'), desc="Launch keepass"),
    Key([mod], "o", lazy.spawn('libreoffice'), desc="Launch Libreoffice"),
    Key([mod], "s", lazy.spawn('scrot \'%d-%m-%Y_$Wx$h_scrot.png\' -e \'mv $f ~/Pictures/Screenshots\''), desc="Screenshot"),
    Key([mod], "t", lazy.spawn('turtl'), desc="Launch turtl"),

    ### SWTICH BETWEEN WINDOWS ###
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    ### RESIZE WINDOWS ###
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, 'shift'], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    ### WINDOWS CONTROL  ###
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    ### QTILE COMMANDS ###
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

### GROUPS CONFIGURATIONS ###
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([

        ### MOVE TO THE GROUP  ### 
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),

        ### MOVE FOCUSED WINDOWS BETWEEN GROUPS  ###
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),  desc="move focused window to group {}".format(i.name)),
    ])
    ### GROUPS NUMBER AND NAME ###
    groups = [
        Group("0",
              label=""),

        Group("1",
              label=""),

        Group("2",
              label=""),

        Group("3",
              label=""),

        Group("4",
              label=""),

        Group("5",
              label=""),

        Group("6",
              label=""),

        Group("7",
              label=""),

        Group("8",
              label=""),

    ]
    for i in range(len(groups)):
        keys.append(Key([mod], str((i + 1)), lazy.group[str(i)].toscreen()))
        keys.append(Key([mod, "shift"], str((i + 1)), lazy.window.togroup(str(i), switch_group=True)))

layouts = [
    layout.Max(),
        layout.MonadTall(
        border_focus = '#bd93f9',
        border_normal = '#282a36',
        border_width = 3,
        margin = 7,
        single_margin = 30,
        ),

        layout.RatioTile(
        border_focus = '#bd93f9',
        border_normal = '#282a36',
        border_width = 3,
        margin = 7,
        single_margin = 30,
        )
]

widget_defaults = dict(
    font='Fira Code Bold',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [

                widget.GroupBox(
                    font = 'Fira Code Bold',
                    fontsize = 11,
                    background = '#282a36',
                    foreground = '#ff79c6',
                    active = '#50fa7b',
                    inactive = '#6272a4',
                    this_current_screen_border = '#50fa7b',
                    block_highlight_text_color = '#50fa7b',
                    borderwidth = 2,
                    hide_unused = False,
                    highlight_method = 'line',
                    highlight_color = ['#282a36', '#44475a'],
                    urgent_border = '#ffb86c'
                ),
                widget.Sep(
                     background = '#282a36',
                     foreground = '#44475a',
                     padding = 20,
                     linewidth = 3,
                     size_percent = 100,
                     ),
                widget.Prompt(
                    font = 'Fira Code Bold',
                    fontsize = 11,
                    background = '#282a36',
                    foreground = '#f8f8f2',
                    ),

                widget.WindowName(
                    empty_group_string = 'Welcome, Pedro!',
                    font = 'Fira Code Bold',
                    fontsize = 11,
                    background = '#282a36',
                    foreground = '#ffb86c',
                    ),

                widget.CurrentLayout(
                    background = '#282a36',
                    foreground = '#50fa7b',
                    ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                 widget.Sep(
                     background = '#282a36',
                     foreground = '#44475a',
                     padding = 20,
                     linewidth = 3,
                     size_percent = 100,
                     ),
                widget.Clock(
                    font = 'Fira Code Bold',
                    fontsize = 11,
                    background = '#282a36',
                    foreground = '#ff79c6',
                    format='%d-%m-%Y %a %I:%M %p',
                    ),
                widget.Sep(
                     background = '#282a36',
                     foreground = '#44475a',
                     padding = 20,
                     linewidth = 3,
                     size_percent = 100,
                     ),

                widget.Systray(
                    background = '#282a36',
                    ),

            ],
            25,
        ),
    ),
]
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wmname = ":)"
