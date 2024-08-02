def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for key, values in group_dictionary.items():
		# Now go through the users in the group
		for value in values:
			if value in user_groups:
				user_groups[value].append(key)
			else:
				user_groups[value] = [key]
			# Now add the group to the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user(
    {
        "local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"]
    }))

# Example: 'admin': ['local', 'public', 'administrator']