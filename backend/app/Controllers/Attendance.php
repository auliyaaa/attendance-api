<?php

namespace App\Controllers;

use App\Models\AttendanceModel;
use CodeIgniter\RESTful\ResourceController;

class Attendance extends ResourceController
{
    protected $attendanceModel;

    public function __construct()
    {
        $this->attendanceModel = new AttendanceModel();
    }

    public function index()
    {
        return $this->respond($this->attendanceModel->getAttendance());
    }

    public function attendanceSummary()
    {
        return $this->respond($this->attendanceModel->getAttendanceSummary());
    }
}
