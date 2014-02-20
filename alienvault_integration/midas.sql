		-- IPFW
		-- plugin_id: 1987
		DELETE FROM plugin WHERE id = "1987";
		DELETE FROM plugin_sid where plugin_id = "1987";


		INSERT INTO plugin (id, type, name, description) VALUES (1987, 1, 'MIDAS', 'MIDAS Macosx IDS');

		INSERT INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (1987, 1, NULL, NULL, 'MIDAS: Removed User account' ,1, 1);
		INSERT INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (1987, 2, NULL, NULL, 'MIDAS: New User account' ,1, 1);
		INSERT INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (1987, 3, NULL, NULL, 'MIDAS: Removed Kernel Extension (OS X kext)' ,1, 1);
		INSERT INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (1987, 4, NULL, NULL, 'MIDAS: Changed Kernel Extension (OS X kext)' ,1, 1);
		INSERT INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (1987, 5, NULL, NULL, 'MIDAS: New Kernel Extension (OS X kext)' ,1, 1);
    INSERT INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (1987, 6, NULL, NULL, 'MIDAS: Removed Property List (OS X plist)' ,1, 1);
    INSERT INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (1987, 7, NULL, NULL, 'MIDAS: Changed Property List (OS X plist)' ,1, 1);
    INSERT INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (1987, 8, NULL, NULL, 'MIDAS: New Property List (OS X plist)' ,1, 1);