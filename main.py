import utils
import dearpygui.dearpygui as im


def set_output_val(val):
    def local_theme():
        with im.theme() as global_theme:
            with im.theme_component(im.mvInputText):
                im.add_theme_color(im.mvThemeCol_Text, (0, 200, 0))
        return global_theme

    im.set_value(item="input", value=val)
    im.bind_item_theme(item="input", theme=local_theme())


def input_button_callback(sender, app_data, user_data):
    def local_theme():
        with im.theme() as global_theme:
            with im.theme_component(im.mvInputText):
                im.add_theme_color(im.mvThemeCol_Text, (255, 255, 255))
        return global_theme

    input_val = im.get_value("input")
    im.set_value("input", value=input_val + user_data)
    im.bind_item_theme(item="input", theme=local_theme())


def calc_button_callback():
    input_val = im.get_value("input")
    if input_val != "":
        set_output_val(utils.calc(input_val))


def remove_callback():
    input_val = im.get_value("input")
    if len(input_val) > 0:
        im.set_value(item="input", value=input_val[:len(input_val) - 1])


def main():
    im.create_context()

    with im.window(label="Calculator", tag="win") as win:
        with im.group(horizontal=True):
            im.add_input_text(label="##input", width=270, tag="input")
            #im.add_text("0", tag="input-label")
        with im.group(horizontal=False):
            with im.group(horizontal=True) as t1:
                im.add_button(label="7", width=50, height=50, callback=input_button_callback, user_data="7")
                im.add_button(label="8", width=50, height=50, callback=input_button_callback, user_data="8")
                im.add_button(label="9", width=50, height=50, callback=input_button_callback, user_data="9")
                im.add_button(label="/", width=50, height=50, callback=input_button_callback, user_data="/")
                im.add_button(label="<-", width=50, height=50, callback=remove_callback)
            with im.group(horizontal=True) as t2:
                im.add_button(label="4", width=50, height=50, callback=input_button_callback, user_data="4")
                im.add_button(label="5", width=50, height=50, callback=input_button_callback, user_data="5")
                im.add_button(label="6", width=50, height=50, callback=input_button_callback, user_data="6")
                im.add_button(label="*", width=50, height=50, callback=input_button_callback, user_data="*")
                im.add_button(label="-", width=50, height=50, callback=input_button_callback, user_data="-")
            with im.group(horizontal=True):
                with im.group(horizontal=False):
                    with im.group(horizontal=True) as t1:
                        im.add_button(label="1", width=50, height=50, callback=input_button_callback, user_data="1")
                        im.add_button(label="2", width=50, height=50, callback=input_button_callback, user_data="2")
                        im.add_button(label="3", width=50, height=50, callback=input_button_callback, user_data="3")
                    with im.group(horizontal=True) as t0:
                        im.add_button(label="0", width=105, height=50, callback=input_button_callback, user_data="0")
                        im.add_button(label=",", width=50, height=50, callback=input_button_callback, user_data=".")
                im.add_button(label="+", width=50, height=105, callback=input_button_callback, user_data="+")
                im.add_button(label="=", width=50, height=105, callback=calc_button_callback)

    im.create_viewport(width=302, height=318, resizable=False, title="Calculator", small_icon="./icon.ico", large_icon="./icon.ico")
    utils.fix_icon_for_taskbar(win)
    im.setup_dearpygui()

    im.bind_theme(theme())
    im.show_viewport()
    im.set_primary_window(window="win", value=True)
    im.start_dearpygui()
    im.destroy_context()


def theme():
    with im.theme() as global_theme:
        with im.theme_component(im.mvAll):
            im.add_theme_color(im.mvThemeCol_FrameBg, (33, 33, 34), category=im.mvThemeCat_Core)

            im.add_theme_style(im.mvStyleVar_FrameRounding, 0, category=im.mvThemeCat_Core)
            im.add_theme_style(im.mvStyleVar_WindowBorderSize, 0, category=im.mvThemeCat_Core)
        with im.theme_component(im.mvInputText):
            im.add_theme_color(im.mvThemeCol_FrameBg, (30, 30, 31), category=im.mvThemeCat_Core)
            im.add_theme_style(im.mvStyleVar_FrameRounding, 0, category=im.mvThemeCat_Core)
            im.add_theme_style(im.mvStyleVar_FramePadding, 15, 15, category=im.mvThemeCat_Core)
        with im.theme_component(im.mvGroup):
            im.add_theme_color(im.mvThemeCol_Button, (30, 30, 31), category=im.mvThemeCat_Core)
            im.add_theme_style(im.mvStyleVar_ItemSpacing, 5, 5, category=im.mvThemeCat_Core)

    return global_theme


if __name__ == '__main__':
    main()
