		-- IPFW
		-- plugin_id: 1987
		DELETE FROM plugin WHERE id = "1987";
		DELETE FROM plugin_sid where plugin_id = "1987";


		INSERT INTO plugin (id, type, name, description) VALUES (1987, 1, 'MIDAS', 'MIDAS Macosx IDS');

		INSERT INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (1987, 1, NULL, NULL, 'MIDAS: New User' ,1, 1);
		INSERT INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (1987, 2, NULL, NULL, 'MIDAS: New kernel extension (OS X kext)' ,1, 1);
		INSERT INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (1987, 3, NULL, NULL, 'MIDAS: New Property List (OS X plist)' ,1, 1);
