local addonName = "Altoholic"
local addon = _G[addonName]
local colors = addon.Colors

local L = LibStub("AceLocale-3.0"):GetLocale(addonName)
local ns = addon.Tabs.Shadowlands

addon:Controller("AltoholicUI.ShadowlandsSanctumFeatures", {
	OnBind = function(frame)
		frame:Update()
	end,
	Update = function(frame)
	end,
})
