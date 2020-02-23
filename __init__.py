# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
import nodeitems_utils

bl_info = {
    "name": "Nodes Menu",
    "description": "",
    "author": "kromar",
    "version": (1, 0, 1),
    "blender": (2, 80, 0),
    "location": "NODE_EDITOR",
    "category": "System"
}


def register():
    bpy.types.NODE_PT_active_node_generic.prepend(nodeitems_utils.draw_node_categories_menu)


def unregister():
    bpy.types.NODE_PT_active_node_generic.remove(nodeitems_utils.draw_node_categories_menu)


if __name__ == "__main__":
    register()
