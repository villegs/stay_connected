hospital_data = {
    "Center A": {
        'Number of Patients': 1500,  # Hospital serving a city of 500k
        'Average Time to Get Served': 30,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 10, 'Semi-Urgent': 20, 'Non-Urgent': 45},
        'Patient Satisfaction Scores': 4.2,  # Out of 5
        'Number of Readmissions': 50,
        'Number of Medical Licenses Presented': 100,
        'Number of Staff Training Hours': 500,
        'Utilization of Equiment & Resources': 85,  # Percentage
        'Number of  Supplies Ordered/Consumed': 10000,
        'Turnover Rate of Staff': 10,  # Percentage
        'Average Cost per Patient': 500,
        'Number of Outpatient Appointments': 2000,
        'Number of Emergency Room Visits': 500,
        'Number of Surgical Procedures Performed': 300,
        'Bed Occupancy Rate': 70,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Increasing', 'Income': 'Stable', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Below National Average', 'Length of Stay': 'Slightly Above Average'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Above Average', 'Readmission Rate': 'Below Average'}
    },
    "Center B": {
        'Number of Patients': 1400,  # Hospital serving a city of 500k
        'Average Time to Get Served': 35,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 12, 'Semi-Urgent': 25, 'Non-Urgent': 50},
        'Patient Satisfaction Scores': 4.0,  # Out of 5
        'Number of Readmissions': 60,
        'Number of Medical Licenses Presented': 90,
        'Number of Staff Training Hours': 450,
        'Utilization of Equiment & Resources': 80,  # Percentage
        'Number of  Supplies Ordered/Consumed': 9000,
        'Turnover Rate of Staff': 12,  # Percentage
        'Average Cost per Patient': 480,
        'Number of Outpatient Appointments': 1800,
        'Number of Emergency Room Visits': 450,
        'Number of Surgical Procedures Performed': 280,
        'Bed Occupancy Rate': 65,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Stable', 'Income': 'Slightly Decreasing', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Slightly Above National Average', 'Length of Stay': 'Slightly Above Average'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Average', 'Readmission Rate': 'Slightly Above Average'}
    },
    "Center C": {
        'Number of Patients': 1600,  # Hospital serving a city of 500k
        'Average Time to Get Served': 28,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 8, 'Semi-Urgent': 18, 'Non-Urgent': 40},
        'Patient Satisfaction Scores': 4.4,  # Out of 5
        'Number of Readmissions': 45,
        'Number of Medical Licenses Presented': 110,
        'Number of Staff Training Hours': 600,
        'Utilization of Equiment & Resources': 90,  # Percentage
        'Number of  Supplies Ordered/Consumed': 11000,
        'Turnover Rate of Staff': 8,  # Percentage
        'Average Cost per Patient': 520,
        'Number of Outpatient Appointments': 2200,
        'Number of Emergency Room Visits': 600,
        'Number of Surgical Procedures Performed': 350,
        'Bed Occupancy Rate': 75,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Slightly Decreasing', 'Income': 'Stable', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Below National Average', 'Length of Stay': 'Average'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Above Average', 'Readmission Rate': 'Below Average'}
    },
    "Clinic D": {
        'Number of Patients': 500,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 15,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 5, 'Semi-Urgent': 10, 'Non-Urgent': 20},
        'Patient Satisfaction Scores': 4.1,  # Out of 5
        'Number of Readmissions': 10,
        'Number of Medical Licenses Presented': 20,
        'Number of Staff Training Hours': 150,
        'Utilization of Equiment & Resources': 70,  # Percentage
        'Number of  Supplies Ordered/Consumed': 3000,
        'Turnover Rate of Staff': 15,  # Percentage
        'Average Cost per Patient': 300,
        'Number of Outpatient Appointments': 800,
        'Number of Emergency Room Visits': 50,
        'Number of Surgical Procedures Performed': 20,
        'Bed Occupancy Rate': 50,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Stable', 'Income': 'Slightly Increasing', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Above Average', 'Readmission Rate': 'Below Average'}
    },
    "Clinic E": {
        'Number of Patients': 450,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 18,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 6, 'Semi-Urgent': 12, 'Non-Urgent': 25},
        'Patient Satisfaction Scores': 3.9,  # Out of 5
        'Number of Readmissions': 12,
        'Number of Medical Licenses Presented': 18,
        'Number of Staff Training Hours': 120,
        'Utilization of Equiment & Resources': 65,  # Percentage
        'Number of  Supplies Ordered/Consumed': 2500,
        'Turnover Rate of Staff': 18,  # Percentage
        'Average Cost per Patient': 280,
        'Number of Outpatient Appointments': 700,
        'Number of Emergency Room Visits': 40,
        'Number of Surgical Procedures Performed': 15,
        'Bed Occupancy Rate': 45,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Slightly Decreasing', 'Income': 'Stable', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Average', 'Readmission Rate': 'Slightly Above Average'}
    },
    "Clinic F": {
        'Number of Patients': 350,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 12,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 4, 'Semi-Urgent': 8, 'Non-Urgent': 15},
        'Patient Satisfaction Scores': 4.3,  # Out of 5
        'Number of Readmissions': 8,
        'Number of Medical Licenses Presented': 15,
        'Number of Staff Training Hours': 100,
        'Utilization of Equiment & Resources': 75,  # Percentage
        'Number of  Supplies Ordered/Consumed': 2000,
        'Turnover Rate of Staff': 12,  # Percentage
        'Average Cost per Patient': 250,
        'Number of Outpatient Appointments': 600,
        'Number of Emergency Room Visits': 30,
        'Number of Surgical Procedures Performed': 10,
        'Bed Occupancy Rate': 40,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Slightly Increasing', 'Income': 'Stable', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Above Average', 'Readmission Rate': 'Below Average'}
    },
    "Clinic G": {
        'Number of Patients': 400,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 16,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 5, 'Semi-Urgent': 11, 'Non-Urgent': 22},
        'Patient Satisfaction Scores': 4.0,  # Out of 5
        'Number of Readmissions': 11,
        'Number of Medical Licenses Presented': 16,
        'Number of Staff Training Hours': 110,
        'Utilization of Equiment & Resources': 68,  # Percentage
        'Number of  Supplies Ordered/Consumed': 2300,
        'Turnover Rate of Staff': 16,  # Percentage
        'Average Cost per Patient': 270,
        'Number of Outpatient Appointments': 650,
        'Number of Emergency Room Visits': 35,
        'Number of Surgical Procedures Performed': 12,
        'Bed Occupancy Rate': 42,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Stable', 'Income': 'Slightly Decreasing', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Average', 'Readmission Rate': 'Slightly Above Average'}
    },
    "Clinic H": {
        'Number of Patients': 300,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 10,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 3, 'Semi-Urgent': 7, 'Non-Urgent': 13},
        'Patient Satisfaction Scores': 4.2,  # Out of 5
        'Number of Readmissions': 7,
        'Number of Medical Licenses Presented': 12,
        'Number of Staff Training Hours': 90,
        'Utilization of Equiment & Resources': 72,  # Percentage
        'Number of  Supplies Ordered/Consumed': 1800,
        'Turnover Rate of Staff': 10,  # Percentage
        'Average Cost per Patient': 230,
        'Number of Outpatient Appointments': 500,
        'Number of Emergency Room Visits': 25,
        'Number of Surgical Procedures Performed': 8,
        'Bed Occupancy Rate': 35,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Slightly Increasing', 'Income': 'Stable', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Above Average', 'Readmission Rate': 'Below Average'}
    },
    "Clinic I": {
        'Number of Patients': 250,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 9,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 2, 'Semi-Urgent': 6, 'Non-Urgent': 12},
        'Patient Satisfaction Scores': 4.1,  # Out of 5
        'Number of Readmissions': 6,
        'Number of Medical Licenses Presented': 10,
        'Number of Staff Training Hours': 80,
        'Utilization of Equiment & Resources': 68,  # Percentage
        'Number of  Supplies Ordered/Consumed': 1500,
        'Turnover Rate of Staff': 14,  # Percentage
        'Average Cost per Patient': 220,
        'Number of Outpatient Appointments': 400,
        'Number of Emergency Room Visits': 20,
        'Number of Surgical Procedures Performed': 5,
        'Bed Occupancy Rate': 30,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Stable', 'Income': 'Slightly Decreasing', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Above Average', 'Readmission Rate': 'Below Average'}
    },
    "Clinic J": {
        'Number of Patients': 420,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 14,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 4, 'Semi-Urgent': 9, 'Non-Urgent': 18},
        'Patient Satisfaction Scores': 3.8,  # Out of 5
        'Number of Readmissions': 9,
        'Number of Medical Licenses Presented': 17,
        'Number of Staff Training Hours': 105,
        'Utilization of Equiment & Resources': 66,  # Percentage
        'Number of  Supplies Ordered/Consumed': 2400,
        'Turnover Rate of Staff': 15,  # Percentage
        'Average Cost per Patient': 260,
        'Number of Outpatient Appointments': 680,
        'Number of Emergency Room Visits': 38,
        'Number of Surgical Procedures Performed': 11,
        'Bed Occupancy Rate': 40,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Stable', 'Income': 'Stable', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Average', 'Readmission Rate': 'Slightly Above Average'}
    },
    "Clinic K": {
        'Number of Patients': 380,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 13,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 3, 'Semi-Urgent': 8, 'Non-Urgent': 16},
        'Patient Satisfaction Scores': 4.0,  # Out of 5
        'Number of Readmissions': 8,
        'Number of Medical Licenses Presented': 14,
        'Number of Staff Training Hours': 95,
        'Utilization of Equiment & Resources': 70,  # Percentage
        'Number of  Supplies Ordered/Consumed': 2100,
        'Turnover Rate of Staff': 13,  # Percentage
        'Average Cost per Patient': 240,
        'Number of Outpatient Appointments': 580,
        'Number of Emergency Room Visits': 32,
        'Number of Surgical Procedures Performed': 9,
        'Bed Occupancy Rate': 38,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Slightly Increasing', 'Income': 'Slightly Increasing', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Average', 'Readmission Rate': 'Slightly Above Average'}
    },
    "Clinic L": {
        'Number of Patients': 280,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 11,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 3, 'Semi-Urgent': 7, 'Non-Urgent': 14},
        'Patient Satisfaction Scores': 4.3,  # Out of 5
        'Number of Readmissions': 5,
        'Number of Medical Licenses Presented': 11,
        'Number of Staff Training Hours': 85,
        'Utilization of Equiment & Resources': 68,  # Percentage
        'Number of  Supplies Ordered/Consumed': 1600,
        'Turnover Rate of Staff': 12,  # Percentage
        'Average Cost per Patient': 210,
        'Number of Outpatient Appointments': 450,
        'Number of Emergency Room Visits': 22,
        'Number of Surgical Procedures Performed': 6,
        'Bed Occupancy Rate': 32,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Stable', 'Income': 'Stable', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Above Average', 'Readmission Rate': 'Below Average'}
    },
    "Clinic M": {
        'Number of Patients': 320,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 12,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 3, 'Semi-Urgent': 8, 'Non-Urgent': 15},
        'Patient Satisfaction Scores': 3.9,  # Out of 5
        'Number of Readmissions': 7,
        'Number of Medical Licenses Presented': 13,
        'Number of Staff Training Hours': 90,
        'Utilization of Equiment & Resources': 65,  # Percentage
        'Number of  Supplies Ordered/Consumed': 1800,
        'Turnover Rate of Staff': 14,  # Percentage
        'Average Cost per Patient': 225,
        'Number of Outpatient Appointments': 520,
        'Number of Emergency Room Visits': 28,
        'Number of Surgical Procedures Performed': 7,
        'Bed Occupancy Rate': 35,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Slightly Decreasing', 'Income': 'Stable', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Average', 'Readmission Rate': 'Slightly Above Average'}
    },
    "Clinic N": {
        'Number of Patients': 260,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 10,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 2, 'Semi-Urgent': 6, 'Non-Urgent': 13},
        'Patient Satisfaction Scores': 4.2,  # Out of 5
        'Number of Readmissions': 4,
        'Number of Medical Licenses Presented': 10,
        'Number of Staff Training Hours': 75,
        'Utilization of Equiment & Resources': 68,  # Percentage
        'Number of  Supplies Ordered/Consumed': 1400,
        'Turnover Rate of Staff': 11,  # Percentage
        'Average Cost per Patient': 200,
        'Number of Outpatient Appointments': 420,
        'Number of Emergency Room Visits': 21,
        'Number of Surgical Procedures Performed': 4,
        'Bed Occupancy Rate': 30,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Stable', 'Income': 'Slightly Increasing', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Above Average', 'Readmission Rate': 'Below Average'}
    },
    "Clinic O": {
        'Number of Patients': 360,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 13,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 4, 'Semi-Urgent': 8, 'Non-Urgent': 17},
        'Patient Satisfaction Scores': 3.9,  # Out of 5
        'Number of Readmissions': 8,
        'Number of Medical Licenses Presented': 14,
        'Number of Staff Training Hours': 95,
        'Utilization of Equiment & Resources': 66,  # Percentage
        'Number of  Supplies Ordered/Consumed': 1900,
        'Turnover Rate of Staff': 13,  # Percentage
        'Average Cost per Patient': 235,
        'Number of Outpatient Appointments': 560,
        'Number of Emergency Room Visits': 29,
        'Number of Surgical Procedures Performed': 8,
        'Bed Occupancy Rate': 37,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Stable', 'Income': 'Stable', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Average', 'Readmission Rate': 'Slightly Above Average'}
    },
    "Clinic P": {
        'Number of Patients': 240,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 9,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 2, 'Semi-Urgent': 5, 'Non-Urgent': 11},
        'Patient Satisfaction Scores': 4.4,  # Out of 5
        'Number of Readmissions': 5,
        'Number of Medical Licenses Presented': 9,
        'Number of Staff Training Hours': 70,
        'Utilization of Equiment & Resources': 70,  # Percentage
        'Number of  Supplies Ordered/Consumed': 1300,
        'Turnover Rate of Staff': 10,  # Percentage
        'Average Cost per Patient': 190,
        'Number of Outpatient Appointments': 380,
        'Number of Emergency Room Visits': 18,
        'Number of Surgical Procedures Performed': 3,
        'Bed Occupancy Rate': 28,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Slightly Increasing', 'Income': 'Slightly Increasing', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Above Average', 'Readmission Rate': 'Below Average'}
    },
    "Clinic Q": {
        'Number of Patients': 340,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 12,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 3, 'Semi-Urgent': 7, 'Non-Urgent': 16},
        'Patient Satisfaction Scores': 4.0,  # Out of 5
        'Number of Readmissions': 6,
        'Number of Medical Licenses Presented': 13,
        'Number of Staff Training Hours': 90,
        'Utilization of Equiment & Resources': 65,  # Percentage
        'Number of  Supplies Ordered/Consumed': 1800,
        'Turnover Rate of Staff': 12,  # Percentage
        'Average Cost per Patient': 220,
        'Number of Outpatient Appointments': 540,
        'Number of Emergency Room Visits': 27,
        'Number of Surgical Procedures Performed': 7,
        'Bed Occupancy Rate': 35,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Stable', 'Income': 'Stable', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Average', 'Readmission Rate': 'Slightly Above Average'}
    },
    "Clinic R": {
        'Number of Patients': 220,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 8,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 2, 'Semi-Urgent': 5, 'Non-Urgent': 10},
        'Patient Satisfaction Scores': 4.3,  # Out of 5
        'Number of Readmissions': 4,
        'Number of Medical Licenses Presented': 8,
        'Number of Staff Training Hours': 65,
        'Utilization of Equiment & Resources': 68,  # Percentage
        'Number of  Supplies Ordered/Consumed': 1200,
        'Turnover Rate of Staff': 9,  # Percentage
        'Average Cost per Patient': 180,
        'Number of Outpatient Appointments': 360,
        'Number of Emergency Room Visits': 17,
        'Number of Surgical Procedures Performed': 3,
        'Bed Occupancy Rate': 25,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Slightly Decreasing', 'Income': 'Slightly Increasing', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Above Average', 'Readmission Rate': 'Below Average'}
    },
    "Clinic S": {
        'Number of Patients': 300,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 11,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 3, 'Semi-Urgent': 6, 'Non-Urgent': 14},
        'Patient Satisfaction Scores': 4.1,  # Out of 5
        'Number of Readmissions': 5,
        'Number of Medical Licenses Presented': 12,
        'Number of Staff Training Hours': 80,
        'Utilization of Equiment & Resources': 65,  # Percentage
        'Number of  Supplies Ordered/Consumed': 1700,
        'Turnover Rate of Staff': 11,  # Percentage
        'Average Cost per Patient': 210,
        'Number of Outpatient Appointments': 480,
        'Number of Emergency Room Visits': 24,
        'Number of Surgical Procedures Performed': 6,
        'Bed Occupancy Rate': 32,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Stable', 'Income': 'Stable', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Above Average', 'Readmission Rate': 'Below Average'}
    },
    "Clinic T": {
        'Number of Patients': 200,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 7,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 1, 'Semi-Urgent': 4, 'Non-Urgent': 9},
        'Patient Satisfaction Scores': 4.2,  # Out of 5
        'Number of Readmissions': 3,
        'Number of Medical Licenses Presented': 7,
        'Number of Staff Training Hours': 60,
        'Utilization of Equiment & Resources': 68,  # Percentage
        'Number of  Supplies Ordered/Consumed': 1100,
        'Turnover Rate of Staff': 8,  # Percentage
        'Average Cost per Patient': 170,
        'Number of Outpatient Appointments': 340,
        'Number of Emergency Room Visits': 15,
        'Number of Surgical Procedures Performed': 2,
        'Bed Occupancy Rate': 23,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Slightly Increasing', 'Income': 'Stable', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Above Average', 'Readmission Rate': 'Below Average'}
    },
    "Clinic U": {
        'Number of Patients': 280,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 10,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 2, 'Semi-Urgent': 6, 'Non-Urgent': 12},
        'Patient Satisfaction Scores': 3.9,  # Out of 5
        'Number of Readmissions': 5,
        'Number of Medical Licenses Presented': 11,
        'Number of Staff Training Hours': 75,
        'Utilization of Equiment & Resources': 63,  # Percentage
        'Number of  Supplies Ordered/Consumed': 1500,
        'Turnover Rate of Staff': 10,  # Percentage
        'Average Cost per Patient': 200,
        'Number of Outpatient Appointments': 440,
        'Number of Emergency Room Visits': 20,
        'Number of Surgical Procedures Performed': 5,
        'Bed Occupancy Rate': 28,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Stable', 'Income': 'Slightly Decreasing', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Average', 'Readmission Rate': 'Slightly Above Average'}
    },
    "Clinic V": {
        'Number of Patients': 180,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 6,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 1, 'Semi-Urgent': 3, 'Non-Urgent': 8},
        'Patient Satisfaction Scores': 4.5,  # Out of 5
        'Number of Readmissions': 2,
        'Number of Medical Licenses Presented': 6,
        'Number of Staff Training Hours': 50,
        'Utilization of Equiment & Resources': 68,  # Percentage
        'Number of  Supplies Ordered/Consumed': 900,
        'Turnover Rate of Staff': 7,  # Percentage
        'Average Cost per Patient': 150,
        'Number of Outpatient Appointments': 300,
        'Number of Emergency Room Visits': 12,
        'Number of Surgical Procedures Performed': 1,
        'Bed Occupancy Rate': 20,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Slightly Increasing', 'Income': 'Slightly Increasing', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Above Average', 'Readmission Rate': 'Below Average'}
    },
    "Clinic W": {
        'Number of Patients': 260,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 9,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 2, 'Semi-Urgent': 5, 'Non-Urgent': 11},
        'Patient Satisfaction Scores': 4.0,  # Out of 5
        'Number of Readmissions': 4,
        'Number of Medical Licenses Presented': 10,
        'Number of Staff Training Hours': 70,
        'Utilization of Equiment & Resources': 65,  # Percentage
        'Number of  Supplies Ordered/Consumed': 1400,
        'Turnover Rate of Staff': 10,  # Percentage
        'Average Cost per Patient': 190,
        'Number of Outpatient Appointments': 420,
        'Number of Emergency Room Visits': 19,
        'Number of Surgical Procedures Performed': 4,
        'Bed Occupancy Rate': 28,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Stable', 'Income': 'Stable', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Average', 'Readmission Rate': 'Slightly Above Average'}
    },
    "Clinic X": {
        'Number of Patients': 160,  # Clinic serving 20k to 50k people
        'Average Time to Get Served': 5,  # Minutes
        'Average Time to Get Served by Urgency Level': {'Urgent': 1, 'Semi-Urgent': 2, 'Non-Urgent': 7},
        'Patient Satisfaction Scores': 4.4,  # Out of 5
        'Number of Readmissions': 2,
        'Number of Medical Licenses Presented': 5,
        'Number of Staff Training Hours': 45,
        'Utilization of Equiment & Resources': 68,  # Percentage
        'Number of  Supplies Ordered/Consumed': 800,
        'Turnover Rate of Staff': 6,  # Percentage
        'Average Cost per Patient': 140,
        'Number of Outpatient Appointments': 280,
        'Number of Emergency Room Visits': 10,
        'Number of Surgical Procedures Performed': 1,
        'Bed Occupancy Rate': 18,  # Percentage
        'Trends in Patient Demographics': {'Age': 'Slightly Decreasing', 'Income': 'Slightly Increasing', 'Ethnicity': 'Diverse'},
        'Analysis of Patient Outcomes': {'Mortality Rate': 'Not Applicable', 'Length of Stay': 'Not Applicable'},
        'Comparison of Performance to Benchmarks': {'Patient Satisfaction': 'Above Average', 'Readmission Rate':'Slightly Above Average'}
    }
}

