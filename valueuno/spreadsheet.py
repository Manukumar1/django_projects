# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:12:41 2019

@author: Manukumar Rudresh
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class NextDay:
    def calculateNextDay(daysToRead):
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        # scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            'C:\\Users\\Dell\\Documents\\django_project\\NextDayPredictor.json', scope)
        client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("N50 Cluster Private").sheet1

        # Extract and print all of the values
        list_of_hashes = sheet.get_all_records()

        second_column = []
        third_column = []
        simple_cluster = []
        cluster = []
        dates_column = []
        dates_simple_cluster = []
        dates_cluster = []
        answer = []
        final_answer = []
        simple_cluster = []
        cluster = []
        daysToReadInt = int(daysToRead)
        second_column = sheet.col_values(3)

        third_column = sheet.col_values(4)

        dates_column = sheet.col_values(1)

        simple_cluster = second_column[-(daysToReadInt):]

        cluster = third_column[-(daysToReadInt):]

        if daysToReadInt == 2:
            context = {}
            for i in range(len(second_column) - (1 + daysToReadInt)):
                if ((second_column[i] == simple_cluster[0]) and (second_column[i + 1] == simple_cluster[1])):
                    dates_simple_cluster.append(dates_column[i + 2])
                    answer.append(second_column[i + 2])
            context = dict(zip(dates_simple_cluster,answer))
            return context
        elif daysToReadInt == 3:
            context = {}
            for i in range(len(second_column) - (1 + daysToReadInt)):
                if ((second_column[i] == simple_cluster[0]) and (second_column[i + 1] == simple_cluster[1]) and (
                        second_column[i + 2] == simple_cluster[2])):
                    dates_simple_cluster.append(dates_column[i + 3])
                    answer.append(second_column[i + 3])
            context = dict(zip(dates_simple_cluster, answer))
            return context
        elif daysToReadInt == 4:
            context = {}
            for i in range(len(second_column) - (1 + daysToReadInt)):
                if ((second_column[i] == simple_cluster[0]) and (second_column[i + 1] == simple_cluster[1]) and (
                        second_column[i + 2] == simple_cluster[2]) and (second_column[i + 3] == simple_cluster[3])):
                    dates_simple_cluster.append(dates_column[i + 4])
                    answer.append(second_column[i + 4])
            context = dict(zip(dates_simple_cluster, answer))
            return context
        else:
            context = {}
            for i in range(len(second_column) - (1 + daysToReadInt)):
                if ((second_column[i] == simple_cluster[0]) and (second_column[i + 1] == simple_cluster[1]) and (
                        second_column[i + 2] == simple_cluster[2]) and (second_column[i + 3] == simple_cluster[3]) and (
                        second_column[i + 4] == simple_cluster[4])):
                    dates_simple_cluster.append(dates_column[i + 5])
                    answer.append(second_column[i + 5])
            context = dict(zip(dates_simple_cluster, answer))
            return context

# if __name__ == "__main__":
# #     calculateNextDay()
