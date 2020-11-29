local addonName = "Altoholic"
local addon = _G[addonName]
local colors = addon.Colors

local L = LibStub("AceLocale-3.0"):GetLocale(addonName)
local ns = addon.Tabs.Shadowlands

addon:Controller("AltoholicUI.ShadowlandsOverview", {
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

addon:Controller("AltoholicUI.ShadowlandsRenownButton", {
	OnBind = function(self)
        self:SetPoint("TOPLEFT", self:GetParent().Title, "BOTTOMLEFT")
	end,

    Update = function(self)
	   self:UpdateRenownLevel()
	   self:UpdateButtonTextures()
    end,

    Button_OnClick = function(self, button)
        -- open the renown tab
    end,

    UpdateRenownLevel = function(self)
        self.Renown:SetText(DataStore:GetRenownLevel(ns:GetAltKey()))
    end,

    UpdateButtonTextures = function(self) 
	    local covenantData = C_Covenants.GetCovenantData(DataStore:GetCovenantID(ns:GetAltKey()) or 0)
        if not covenantData then return end
	    self:SetNormalAtlas(("shadowlands-landingpage-renownbutton-%s"):format(covenantData.textureKit));
	    self:SetPushedAtlas(("shadowlands-landingpage-renownbutton-%s"):format(covenantData.textureKit));
	    self.PushedImage:SetAtlas(("shadowlands-landingpage-renownbutton-%s-down"):format(covenantData.textureKit));
    end,

    OnMouseDown = function(self)
	    self.PushedImage:Show();
    end,

    OnMouseUp = function(self)
	    self.PushedImage:Hide();
    end,
})

addon:Controller("AltoholicUI.ShadowlandsSoulbindButton", {
	OnBind = function(self)
        self:SetPoint("TOPLEFT", self:GetParent().RenownButton, "BOTTOMLEFT")
	end,

    Update = function(self)
	   self:UpdateSoulbindName()
    end,

    Button_OnClick = function(self, button)
        -- open the renown tab
    end,

    UpdateSoulbindName = function(self)
	   local soulbindID = DataStore:GetActiveSoulbindID(ns:GetAltKey())
	   if soulbindID > 0 then
    		self:SetSoulbind(C_Soulbinds.GetSoulbindData(soulbindID))
	   end
    end,
    
    OnEnter = function(self)
	   self.Highlight:Show();
    end,

    OnLeave = function(self)
	   self.Highlight:Hide();
    end,

    OnMouseDown = function(self)
	   self.Press:Show();
    end,

    OnMouseUp = function(self)
	   self.Press:Hide();
    end,
    
    SetSoulbind = function(self, soulbindData)
	   local portraitAtlas = ("shadowlands-landingpage-soulbindsbutton-%s"):format(soulbindData.textureKit);
	   self.Portrait:SetAtlas(portraitAtlas, true);
	   self.Label:SetText(soulbindData.name);
    end,
})
