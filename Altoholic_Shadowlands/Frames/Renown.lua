local addonName = "Altoholic"
local addon = _G[addonName]
local colors = addon.Colors

local L = LibStub("AceLocale-3.0"):GetLocale(addonName)
local ns = addon.Tabs.Shadowlands

addon:Controller("AltoholicUI.ShadowlandsRenown", {
	OnBind = function(frame)
		frame:Update()
	end,
	Update = function(frame)
        local key = ns:GetAltKey()
        local covenantData = C_Covenants.GetCovenantData(DataStore:GetCovenantID(key) or 0)

        if covenantData and covenantData.name then	
            frame.Title:SetText(covenantData.name)
        else
            frame.Title:SetText("")
        end
        
		frame:Show()
	end,
})
