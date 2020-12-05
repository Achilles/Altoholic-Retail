local addonName = "Altoholic"
local addon = _G[addonName]
local colors = addon.Colors
local L = LibStub("AceLocale-3.0"):GetLocale(addonName)

addon.Tabs.Shadowlands = {}

local ns = addon.Tabs.Shadowlands

local THIS_ACCOUNT = "Default"
local currentAccount = THIS_ACCOUNT
local currentRealm = GetRealmName()
local currentAlt = UnitName("player")
local currentPanel

-- ** Utility **
local DDM_AddTitle = addon.Helpers.DDM_AddTitle
local DDM_AddCloseMenu = addon.Helpers.DDM_AddCloseMenu

local function GetCharacterLoginText(character)
	local last = DataStore:GetLastLogout(character)
	local _, realm, name = strsplit(".", character)
	
	if last then
		if (realm == GetRealmName()) and (name == UnitName("player")) then
			last = colors.green..GUILD_ONLINE_LABEL
		else
			last = format("%s: %s", LASTONLINE, colors.yellow..date("%m/%d/%Y %H:%M", last))
		end
	else
		last = format("%s: %s", LASTONLINE, colors.red..L["N/A"])
	end
	return format("%s %s(%s%s)", (DataStore:GetColoredCharacterName(character) or ""), colors.white, last, colors.white)
end

-- ** DB / Get **
function ns:GetAccount()
	return currentAccount
end

function ns:GetRealm()
	return currentRealm, currentAccount
end


function ns:GetAlt()
	return currentAlt, currentRealm, currentAccount
end

function ns:GetAltKey()
	if currentAlt and currentRealm and currentAccount then
		return format("%s.%s.%s", currentAccount, currentRealm, currentAlt)
	end
end

-- ** DB / Set **
function ns:SetAlt(alt, realm, account)
	currentAlt = alt
	currentRealm = realm
	currentAccount = account
end

function ns:SetAltKey(key)
	local account, realm, char = strsplit(".", key)
	ns:SetAlt(char, realm, account)
end

-- ** Icon events **
local function OnCharacterChange(self)
	ns:SetAltKey(self.value)
	
	CloseDropDownMenus()
	AltoholicTabShadowlands:Refresh()
    
    if not currentPanel then currentPanel = AltoholicTabShadowlands.OverviewPanel end
    
    currentPanel:Hide()
    currentPanel:Update()
end

local function CharactersIcon_Initialize(self, level)
	local currentCharacterKey = ns:GetAltKey()
    local currentAccount, currentRealm, currentName = strsplit(".", currentCharacterKey)
    
	if level == 1 then
		DDM_AddTitle(L["Characters"])
		
		for account in pairs(DataStore:GetAccounts()) do
			for realm in pairs(DataStore:GetRealms(account)) do

				local info = UIDropDownMenu_CreateInfo()

				info.text = realm
				info.hasArrow = 1
				info.checked = (currentRealm == realm)
				info.value = format("%s.%s", account, realm)
				info.func = nil
				UIDropDownMenu_AddButton(info, level)
			end
		end

		DDM_AddCloseMenu()

	elseif level == 2 then
		local menuAccount, menuRealm = strsplit(".", UIDROPDOWNMENU_MENU_VALUE)
		
		local nameList = {}		-- we want to list characters alphabetically
		for _, character in pairs(DataStore:GetCharacters(menuRealm, menuAccount)) do
			table.insert(nameList, character)	-- we can add the key instead of just the name, since they will all be like account.realm.name, where account & realm are identical
		end
		table.sort(nameList)
		

		for _, character in ipairs(nameList) do
			
			local info = UIDropDownMenu_CreateInfo()
			
			info.text		= GetCharacterLoginText(character)
			info.value		= character
			info.func		= OnCharacterChange
			info.icon		= nil
			info.checked	= (currentCharacterKey == character)
			UIDropDownMenu_AddButton(info, level)
		end
	end
end

function ns:Icon_OnEnter(icon)
	addon:DDM_Initialize(AltoholicTabShadowlands.ContextualMenu, CharactersIcon_Initialize)
	CloseDropDownMenus()
	ToggleDropDownMenu(1, nil, AltoholicTabShadowlands.ContextualMenu, icon, 0, -5)
end

addon:Controller("AltoholicUI.TabShadowlands", {
	OnBind = function(frame)
        -- Setup aliases
        frame.Overview = frame.MenuItem1
        frame.Renown = frame.MenuItem2
        frame.Soulbinds = frame.MenuItem3
        frame.SanctumFeatures = frame.MenuItem4
        frame.Conduits = frame.MenuItem5
        
		-- Localise section names
        frame.Overview:SetText(OVERVIEW)
		frame.Renown:SetText(COVENANT_SANCTUM_TAB_RENOWN)
        frame.Soulbinds:SetText(COVENANT_PREVIEW_SOULBINDS)
        frame.SanctumFeatures:SetText(COVENANT_PREVIEW_SANCTUM_FEATURE)
        frame.Conduits:SetText(ANIMA_DIVERSION_ORIGIN_TOOLTIP)
		
        -- Set section 1 as default
        frame:MenuItem_Highlight(1)
        
        frame.CharactersIcon.Icon:SetTexture(addon:GetCharacterIcon())
        
        frame:Refresh()
	end,
	HideAll = function(frame)
		frame.OverviewPanel:Hide()
		frame.RenownPanel:Hide()
        frame.SoulbindsPanel:Hide()
        frame.SanctumFeaturesPanel:Hide()
        frame.ConduitPanel:Hide()
	end,
	Refresh = function(frame)
        local key = ns:GetAltKey()
        local covenantData = C_Covenants.GetCovenantData(DataStore:GetCovenantID(key) or 0)
        
        if covenantData and covenantData.textureKit then
			AltoholicTabShadowlands.Background:SetAtlas(("ShadowlandsMissionsLandingPage-Background-%s"):format(covenantData.textureKit));
        else
        	AltoholicTabShadowlands.Background:SetAtlas(nil);
        end
	end,
	MenuItem_Highlight = function(frame, id)
		-- highlight the current menu item
		for i = 1, 5 do 
			frame["MenuItem"..i]:UnlockHighlight()
		end
		frame["MenuItem"..id]:LockHighlight()
	end,
	MenuItem_OnClick = function(frame, id, panel)
		frame:HideAll()
		frame:MenuItem_Highlight(id)
		
		if panel then
			frame[panel]:Update()
            currentPanel = frame[panel]
		end
	end,
})
