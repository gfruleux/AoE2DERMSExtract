import ntpath
import os
from tkinter import filedialog

from aoe2de_rms_gen_obj_parser import GeneratingObjectsParser, const

FILE_OPTION_GEN = dict(defaultextension=".inc", title="Select AoE2DE GeneratingObjects.inc file",
                       initialdir="%s/Steam/steamapps/common/AoE2DE/resources/_common/drs/gamedata_x2" %
                                  os.environ.get("PROGRAMFILES(X86)"),
                       filetypes=[('Generating Objects', "*.inc"), ("All Files", "*.*")])

FILE_OPTION_RMS = dict(defaultextension=".rms", title="Select AoE2DE RMS Map files", multiple=True,
                       initialdir="%s/Steam/steamapps/common/AoE2DE/resources/_common/drs/gamedata_x2" %
                                  os.environ.get("PROGRAMFILES(X86)"),
                       filetypes=[("RMS files", "*.rms"), ("RMS2 files", "*.rms2"), ("All files", "*.*")])


def get_file_name(path):
    head, tail = ntpath.split(path)
    file_name = tail or ntpath.basename(head)
    return file_name


def update_path_and_dir(path_left, path_right):
    path = os.path.join(path_left, path_right)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def get_reduced_map():
    map_size_idx = const.MAP_SIZE_DICT.keys()

    map_res_idx = const.MAP_RESOURCES_DICT.keys()

    game_type_idx = const.GAME_TYPE_DICT.keys()

    return map_size_idx, map_res_idx, game_type_idx


def main():
    path_gen_obj = filedialog.askopenfilename(**FILE_OPTION_GEN)
    path_rms_list = filedialog.askopenfilename(**FILE_OPTION_RMS)

    _path = "generated"
    if not os.path.exists(_path):
        os.makedirs(_path)

    _map_size, _map_res, _game_type = get_reduced_map()

    for path_rms in list(path_rms_list):
        for map_size in _map_size:
            _path_m_s = update_path_and_dir(_path, map_size)
            for map_res in _map_res:
                _path_m_r = update_path_and_dir(_path_m_s, map_res)
                for game_type in _game_type:
                    _path_g_t = update_path_and_dir(_path_m_r, game_type)
                    parser = GeneratingObjectsParser(path_gen_obj, path_rms, map_size, map_res, game_type)
                    parser.run_parsers()
                    path_out = os.path.join(_path_g_t, get_file_name(path_rms))
                    print("Writing " + path_out)
                    with open(path_out, "w") as fp:
                        fp.write(parser.get_result())


if __name__ == '__main__':
    main()
