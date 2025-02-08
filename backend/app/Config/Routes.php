<?php

use CodeIgniter\Router\RouteCollection;

/**
 * @var RouteCollection $routes
 */
$routes->get('/', 'Home::index');
$routes->get('/attendance', 'Attendance::index');
$routes->get('/attendance_summary', 'Attendance::attendanceSummary');
