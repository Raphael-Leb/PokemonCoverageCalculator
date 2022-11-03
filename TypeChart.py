import pandas as pd

types = pd.DataFrame([
			["neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "super", "neutral", "neutral", "neutral", "neutral", "neutral", "immune", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral"],
			["neutral", "not", "super", "not", "neutral", "not", "neutral", "neutral", "super", "neutral", "neutral", "not", "super", "neutral", "neutral", "neutral", "not", "not", "neutral"],
			["neutral", "not", "not", "super", "super", "not", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "not", "neutral", "neutral"],
			["neutral", "super", "not", "not", "not", "super", "neutral", "super", "not", "super", "neutral", "super", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral"],
			["neutral", "neutral", "neutral", "neutral", "not", "neutral", "neutral", "neutral", "super", "not", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "not", "neutral", "neutral"],
			["neutral", "super", "neutral", "neutral", "neutral", "not", "super", "neutral", "neutral", "neutral", "neutral", "neutral", "super", "neutral", "neutral", "neutral", "super", "neutral", "neutral"],
			["neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "super", "super", "not", "not", "neutral", "neutral", "not", "neutral", "super", "neutral"],
			["neutral", "neutral", "neutral", "not", "neutral", "neutral", "not", "not", "super", "neutral", "super", "not", "neutral", "neutral", "neutral", "neutral", "neutral", "not", "neutral"],
			["neutral", "neutral", "super", "super", "immune", "super", "neutral", "not", "neutral", "neutral", "neutral", "neutral", "not", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral"],
			["neutral", "neutral", "neutral", "not", "super", "super", "not", "neutral", "immune", "neutral", "neutral", "not", "super", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral"],
			["neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "super", "neutral", "super", "neutral", "super", "neutral", "neutral", "neutral"],
			["neutral", "super", "neutral", "not", "neutral", "neutral", "not", "neutral", "not", "super", "neutral", "neutral", "super", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral"],
			["not", "not", "super", "super", "neutral", "neutral", "super", "not", "super", "not", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "super", "neutral", "neutral"],
			["immune", "neutral", "neutral", "neutral", "neutral", "neutral", "immune", "not", "neutral", "neutral", "neutral", "not", "neutral", "super", "neutral", "super", "neutral", "neutral", "neutral"],
			["neutral", "not", "not", "not", "not", "super", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral"],
			["neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "super", "neutral", "neutral", "super", "neutral"],
			["not", "super", "neutral", "not", "neutral", "not", "super", "immune", "super", "not", "not", "not", "not", "neutral", "not", "neutral", "not", "not", "neutral"],
			["neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "not", "super", "neutral", "neutral", "neutral", "not", "neutral", "neutral", "immune", "not", "super", "neutral", "neutral"],
			["neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral", "neutral"],
			],
			 index = ["normal","fire","water", "grass", "electric", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy", "none"],
			 columns = ["normal","fire","water", "grass", "electric", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy", "none"],
			 dtype="string")

types.index.name = "defender"
types.columns.name = "attacker" 