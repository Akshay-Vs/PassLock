local LuaConsole = CreateFrame("Frame", "LuaConsole", UIParent)
local inset = 3

BINDING_HEADER_LUACONSOLE = "LuaConsole"
BINDING_NAME_LUACONSOLE = "New LuaConsole"

-- Just a gimmick
local user = UnitName("Local Console").."@"..GetRealmName()

local prefix
local keywords = {}
LuaConsole.KeyWords = keywords
local currTable, currTableName

local typeFormat = {}
LuaConsole.TypeFormat = typeFormat
