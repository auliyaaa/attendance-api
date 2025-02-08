<?php

namespace App\Models;

use CodeIgniter\Model;

class AttendanceModel extends Model
{
    protected $table = 'attendance';
    protected $primaryKey = 'id';
    protected $allowedFields = ['date', 'name', 'time', 'location'];

    public function getAttendance()
    {
        return $this->findAll();
    }

    public function getAttendanceSummary()
    {
        return $this->db->table('attendance_summary')->get()->getResultArray();
    }
}
